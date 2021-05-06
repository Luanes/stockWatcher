from libs.SheetWatcher import SheetWatcher
from libs.StockQuotation import StockQuotation

def handler(event, context):
    client = pymongo.MongoClient("mongodb+srv://awsUser:yHubPassword@ootzchallenge.y7nq4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mongoDB = client.yhub
    
    sheetWatcher = SheetWatcher()
    quotated_stocks = sheetWatcher.get_new_stocks_quotation()
    
    for new_stock_quota in quotated_stocks:
        stock_quota = StockQuotation(new_stock_quota)
        stock_quota.compute(mongoDB)