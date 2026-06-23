stockPrices={
    "AAPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "MICROSOFT": 350
}

total=0

n=int(input("How many stocks do you own? "))

for i in range(n):
    stock=input("Enter stock name: ").upper()
    qty=int(input("Enter quantity: "))

    if stock in stockPrices:
        total+=stockPrices[stock]*qty
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))

print("Result saved to portfolio.txt")