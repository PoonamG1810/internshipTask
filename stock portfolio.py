# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3400,
    "MSFT": 330
}

# Dictionary to store user portfolio
portfolio = {}

# Input stocks
print("Enter stock data (type 'done' to finish):")
while True:
    stock = input("Stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares @ ${price} each = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    try:
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price,Total\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock},{quantity},{price},{value}\n")
            file.write(f"\nTotal Investment,,,{total_value}\n")
        print(f"Portfolio saved to '{filename}'.")
    except Exception as e:
        print("Error saving file:", e)
