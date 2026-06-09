stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}
total_investment = 0
print("Stock Portfolio Tracker")
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}")
    else:
        print("Stock not found.")

print(f"\nTotal Investment Value: ${total_investment}")