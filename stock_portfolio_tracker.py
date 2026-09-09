# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350,
    "AMZN": 180
}

total_investment = 0

print("===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock in stock_prices:
    print(stock, "=", "$", stock_prices[stock])

# Ask user for number of different stocks
number = int(input("\nHow many stocks do you want to add? "))

portfolio = []

# Take stock details from user
for i in range(number):

    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        portfolio.append((stock, quantity, price, investment))

        print("Investment for", stock, "=", "$", investment)

    else:
        print("Stock not available!")

# Display portfolio
print("\n===================================")
print("          YOUR PORTFOLIO")
print("===================================")

for stock, quantity, price, investment in portfolio:
    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Investment: $", investment
    )

print("\nTotal Investment = $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}\n"
        )

    file.write("\nTotal Investment = $" + str(total_investment))

print("\nPortfolio saved successfully in portfolio.txt")
