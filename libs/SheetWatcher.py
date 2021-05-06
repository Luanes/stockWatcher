import gspread
import pymongo
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime,date

client = pymongo.MongoClient("mongodb+srv://awsUser:yHubPassword@ootzchallenge.y7nq4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mongoDB = client.yhub

class SheetWatcher:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.spreadsheet = self.client.open("Acoes")
        
    def get_stock_sheet(self):
        return self.spreadsheet.worksheet("Stocks") 
        
    def get_stock_quotation_sheet(self):
        return self.spreadsheet.worksheet("Quotation") 
        
    #This method is too similar to check_stocks_quotated. Refactoration candidate
    def get_untracked_stocks(self, stock_list):
        results = mongoDB.stocks.find({"stock_name": {"$in": stock_list}})
        
        for result in results:
            #If the stock is on the database, it's already been tracked. Then pop the the name from the tracked list
            if result["stock_name"] in stock_list:
                stock_list.pop(stock_list.index(result["stock_name"]))
        return stock_list
    
    #This method is too similar to get_untracked_stocks. Refactoration candidate
    def check_stocks_quotated(self, stock_list):
        results = mongoDB.daily_quotation.find({"stock_name": {"$in": stock_list}, "quotation_date": str(date.today())})
        
        for result in results:
            #If the stock is on the database, it's already been tracked. Then pop the the name
            if result["stock_name"] in stock_list:
                stock_list.pop(stock_list.index(result["stock_name"]))
        return stock_list

    def get_stocks_names(self):
        stocksheet = self.get_stock_sheet()
        stock_names = stocksheet.col_values(1)
        
        #Popping the first item, it's the spreadsheet header.
        stock_names.pop(0)
        return stock_names
        
    def check_new_stocks(self):
        stock_list = self.get_stocks_names()
        untracked_stocks = self.get_untracked_stocks(stock_list)
        
        if (untracked_stocks):
            print("New stocks needed to be added.")
            new_stocks = self.get_new_stock_information(untracked_stocks)
            return new_stocks
            
        else:
            print("No new stocks to add.")
            return []
    
    def get_new_stock_information(self, untracked_stocks):
        stocksheet = self.get_stock_sheet()
        new_stocks = []
        
        #Check for the name of each untracked_stock found on the sheet
        for untracked_stock in untracked_stocks:
            cell = stocksheet.find(untracked_stock)
            new_stock = {
                "stock_name" : untracked_stock,
                "currency" : stocksheet.cell(cell.row, 2).value,
                "stock_market" : stocksheet.cell(cell.row, 3).value
            }
            new_stocks.append(new_stock)
        return new_stocks
        
    def get_new_stocks_quotation(self):
        new_stock_quotations = []
        
        stock_quotation_sheet = self.get_stock_quotation_sheet()
        stock_names = list(set(stock_quotation_sheet.row_values(1)))
        stock_names.pop(stock_names.index(''))
        stock_names = self.check_stocks_quotated(stock_names)
        
        for stock_name in stock_names:
            cell = stock_quotation_sheet.find(stock_name)
            try:
                new_stock_quotation = {
                    "stock_name" : stock_name,
                    "quotation_datetime" : datetime.now(),
                    "high" : float(stock_quotation_sheet.cell(3, cell.col).value),
                    "low" : float(stock_quotation_sheet.cell(5, cell.col).value),
                    "close" : float(stock_quotation_sheet.cell(7, cell.col).value)
                }
                new_stock_quotations.append(new_stock_quotation)
            except:
                print(f'Stock {stock_name} values cannot be converted to float.')
                
        print(f'Generated {len(new_stock_quotations)} quotations.')
        return new_stock_quotations