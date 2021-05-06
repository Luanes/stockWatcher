class Stock:
    def __init__(self, stock_params : dict):
        self.stock_name = stock_params["stock_name"]
        self.currency = stock_params["currency"]
        self.stock_market = stock_params["stock_market"]
        self.validate()
        
    @property
    def sheet_tab(self):
        return "Stocks"
    
    @property    
    def index_route(self):
        return "stocks"
        
    @property
    def data_columns():
        return ["stock_name","currency","stock_market"]
        
    def validate(self):
        if not isinstance(self.stock_name, str):
            raise Exception("Stock name must be a string")
        if not isinstance(self.currency, str):
            raise Exception("Currency must be a string")
        if not isinstance(self.stock_market, str):
            raise Exception("Stock market must be a string")
        
    def compute(self, mongoDB):
        mongo_data_payload = {
            "_id": self.stock_name,
            "stock_name" : self.stock_name,
            "currency" : self.currency,
            "stock_market" :  self.stock_market,
        }
        
        print(mongo_data_payload)
        mongoDB.stocks.insert_one(mongo_data_payload)
        
        