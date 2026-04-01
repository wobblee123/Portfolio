import time
carStorage = {}
carStorageNumber = 0

#adding
def addCar():
    global carStorageNumber
    carModelAdd = input("What model is your car?\n> ").lower()
    carMakeAdd = input("What make is your car?\n> ").lower()
    registrationPlateAdd = input("Enter your car's registration.\n> ")
    carStorageNumber += 1
    print(f"Your car's storage number is {carStorageNumber}.")

    #format
    carFormat = f" Storage Number: {carStorageNumber} | Model: {carModelAdd.capitalize()} | Make: {carMakeAdd.capitalize()} | Registration: {registrationPlateAdd.upper()}" #got helpered
    carStorage[carStorageNumber] = carFormat

#removing
def removeCar():
    try:
        storageNumberRemove = int(input("What is your car's storage number?\n> "))
        if storageNumberRemove in carStorage:
            del carStorage[carStorageNumber]
            print(f"Car with the storage number{storageNumberRemove} was removed from the storage.")
        else:
            print("Car is already non-existant.")

    except ValueError:
        print("Try entering a number!")

#formatting
def storageCheck():
    for v, carStuff in carStorage.items():#got helpered
        print(carStuff)

#looping
while True:
    choice = input("What would you like to do?\n1. Add a car\n2. Remove a car\n3. Check storage\n4. Quit\n >> ").strip()
    if choice == "1":
        addCar()
    elif choice == "2":
        removeCar()
    elif choice == "3":
        storageCheck()
        time.sleep(2)
    elif choice == "4":
        break
    else:
        print("Bad choice!")