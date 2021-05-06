import pymongo
from libs.Stock import Stock
from libs.SheetWatcher import SheetWatcher

def handler(event, context):
    client = pymongo.MongoClient("mongodb+srv://awsUser:yHubPassword@ootzchallenge.y7nq4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mongoDB = client.yhub
    
    sheetWatcher = SheetWatcher()
    new_stocks = sheetWatcher.check_new_stocks()
    
    for new_stock in new_stocks:
        stock = Stock(new_stock)
        stock.compute(mongoDB)