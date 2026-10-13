class Stock_class:
    def __init__(self, symbol, current_price):
        self.symbol = symbol
        self.current_price = current_price

    @property
    def current_price(self):
        return self.current_price 