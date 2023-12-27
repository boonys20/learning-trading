from stock import Stock
import pandas as pd

if __name__ == "__main__":
    set50_request = pd.read_html('https://en.wikipedia.org/wiki/SET50_Index_and_SET100_Index')
    set50_stock = set50_request[0]
    for index, row in set50_stock.iterrows():
        Stock(f'{row["SET Symbol"]}.BK',f'{row["Sector"]}').scrap_data()
