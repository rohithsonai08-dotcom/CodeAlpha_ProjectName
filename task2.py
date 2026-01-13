import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

total_investment = 0
portfolio = []

print(" Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' to stop\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print(" Stock not found\n")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append([stock, price, quantity, investment])

    print(f"{stock} value: ₹{investment}\n")

print("Total Investment Value: ", total_investment)

# Save to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock Name",
                     "Price",
                     "Quantity",
                     "Investment Value"])
    writer.writerows(portfolio)
    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total_investment])

print("Data saved to portfolio.csv")
