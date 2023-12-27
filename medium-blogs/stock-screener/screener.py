# Stocks Screener class
class StockScreener:
    def __init__(self, stocks, filters):
        self.stocks = stocks
        self.filters = filters

    # Add data to stocks
    def add_data(self):
        for stock in self.stocks:
            stock.scrape_data()
            stock.get_stock_price()
    
    def apply_filters(self):
        filtered_stocks = []
        for stock in self.stocks:
            passed_all_filters = True
            for filter_func in self.filters:
                if not filter_func(stock):
                    passed_all_filters = False
            
