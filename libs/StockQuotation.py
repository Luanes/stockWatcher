import pymongo
from datetime import date

class StockQuotation:
    def __init__(self, stock_params : dict):
        self.stock_name = stock_params["stock_name"]
        self.high = stock_params["high"]
        self.low = stock_params["low"]
        self.close = stock_params["close"]
        self.validate()
    
    @property
    def sheet_tab(self):
        return "Quotation"
    
    @property    
    def index_route(self):
        return "daily_quotation"
        
    def validate(self):
        if not isinstance(self.stock_name, str):
            raise Exception("Stock name must be a string.")
        if not isinstance(self.high, float):
            raise Exception("High must be a float.")
        if not isinstance(self.low, float):
            raise Exception("Low market must be a float.")
        if not isinstance(self.close, float):
            raise Exception("Close must be a float.")
        
    def compute(self, mongoDB):
        mongo_data_payload = {
            "_id": self.stock_name+ "-" +str(date.today()),
            "quotation_date": str(date.today()),
            "stock_name": self.stock_name,
            "high" : self.high,
            "low" : self.low,
            "close" :  self.close,
        }
        
        mongoDB.daily_quotation.insert_one(mongo_data_payload)
        
        