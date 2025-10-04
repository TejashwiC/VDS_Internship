class Stock:
    def __init__(self, name, symbol, price_per_share, quantity):
        self.name = name
        self.symbol = symbol
        self.price_per_share = price_per_share
        self.quantity = quantity
    def buy(self, qty):
        self.quantity += qty
        print(f"Bought {qty} shares of {self.symbol}")

    def sell(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
            print(f"Sold {qty} shares of {self.symbol}")
        else:
            print(f"Not enough shares of {self.symbol}! You own only {self.quantity}")

    def total_value(self):
        return self.quantity * self.price_per_share
    def summary(self):
        return f"{self.name} ({self.symbol}) | Shares: {self.quantity} | Price: Rs.{self.price_per_share} | Value: Rs.{self.total_value()}"

portfolio = [
    Stock("Tata Power", "TATAPOWER", 250, 10),
    Stock("Reliance Industries", "RELIANCE", 500, 5)
]
def view_portfolio():
    print("\nPortfolio")
    for stock in portfolio:
        print(stock.summary())
def find_stock(symbol):
    for stock in portfolio:
        if stock.symbol == symbol:
            return stock
    return None
def buy_stock(symbol, qty):
    stock = find_stock(symbol)
    if stock:
        stock.buy(qty)
    else:
        print("Stock not found in portfolio!")
def sell_stock(symbol, qty):
    stock = find_stock(symbol)
    if stock:
        stock.sell(qty)
    else:
        print("Stock not found in portfolio!")

view_portfolio()
buy_stock("TATAPOWER", 10)
buy_stock("RELIANCE", 2)
sell_stock("TATAPOWER", 5)
view_portfolio()
