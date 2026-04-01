#{', '.join(f'\'{k}\'' for k in stock.keys())}\n> ") wasnt me, how am i supposed to know regex

import time

stock = {
    "Apples": 0,
    "Bananas": 0,
    "Cookies": 0
}

def checkstock():
    for item, amount in stock.items():
        print(f" - {item}: {amount}")

while True:
    time.sleep(1)
    print("Welcome to Wobble's shop system for Harry. :)")
    time.sleep(3)
    command = input("Would you like to add, remove, create, delete or check a stock?\n> ").lower().strip()
    time.sleep(1)

    if command == "add":
        stockSelection = input(f"Which stock would you like to add? {', '.join(f'\'{k}\'' for k in stock.keys())}\n> ")
        if stockSelection in stock:
            print("Stock is valid and is found.")
            time.sleep(1)
            addAmount = int(input(f"How much stock would you like to add to {stockSelection}?\n> "))
            stock[stockSelection] += addAmount
            time.sleep(1)
            checkstock()

        else:
            print("Stock not found!")

    elif command == "remove":
        stockSelection = input(f"Which stock would you like to remove from? {', '.join(f'\'{k}\'' for k in stock.keys())}\n> ")
        if stockSelection in stock:
            print("Stock is valid and is found.")
            time.sleep(1)
            removeAmount = int(input(f"How much stock would you like to remove from {stockSelection}?\n> "))
            currentAmount = stock[stockSelection]
            if removeAmount > currentAmount:
                print("Your stock is too low to remove this amount!")

            else:
                stock[stockSelection] -= removeAmount
                time.sleep(1)
                checkstock()

        else:
            print("Stock not found!")

    elif command == "create":
        createStock = input("What is the name of the stock you wish to create?\n> ")
        createStockLower = createStock.lower()

        stockLower = {key.lower(): key for key in stock}

        if createStockLower not in stockLower:
            stock[createStock] = 0
            print(f"{createStock} has been made and add to stock list!")
            time.sleep(1)
            checkstock()

        else:
            print(f"{createStock} already exists as {createStock}!")

    elif command == "delete":
        deleteStock = input(f"What is the name of the stock you wish to delete? {', '.join(f'\'{k}\'' for k in stock.keys())}\n> ")

        if deleteStock in stock:
            del stock[deleteStock]
            print(f"{deleteStock} has been deleted!")
            time.sleep(1)
            checkstock()

        else:
            print(f"{deleteStock} does not exist already!")

    elif command == "check":
        checkstock()

    elif command == "quit":
        break

    else:
        print("Command not recognised!!")