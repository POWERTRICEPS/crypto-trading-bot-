from binance.client import Client
from datafetch import client



#def get_current_price(symbol):
    #ticker = client.get_symbol_ticker(symbol=symbol)
   # return float(ticker['price'])


def place_buy_order(symbol, quantity):
    try:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        return order
    except Exception as e:
        return None

def place_sell_order(symbol, quantity):
    try:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        return order
    except Exception as e:
        return None
    
    
