from binance.client import Client


def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])


def place_buy_order(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    return order

def place_sell_order(symbol, quantity):
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    return order
    
    
