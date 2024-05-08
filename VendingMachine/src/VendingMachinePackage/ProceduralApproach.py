# Assumptions
# 1. Only 5 Drink Items are available in the Vending Machine Scenario.
# 2. Only RM1, RM5, RM10, RM20, RM50 and RM100 notes are accepted for payment.
# 3. Only RM1, RM5, RM10, RM20, RM50 and RM100 notes will be used to return as change.
# 4. Users will not enter any empty inputs when using the Vending Machine.
# 5. Users can only make one drink purchase at a time.

# Program begins here

# function to initialise a list with drinks with their corresponding data attributes
def vendingMachineItems():
    drinkItemsList = ([100, "Americano", 5],[101, "100 Plus", 4],
             [102, "Orange Juice", 6], [103, "Vitagen", 3], [104, "Yakult", 3])
    return drinkItemsList

# function to display all drink items found in the list
def displayItems(drinkItemsList):
    print('---------------------------------')
    print("Vending Machine Drinks")
    print('---------------------------------')
    for i in range(len(drinkItemsList)):
            for j in range(len(drinkItemsList[i])):
                if j==0:
                    print('Item ID: ' + str(drinkItemsList[i][j]))
                elif j==1:
                    print('Name of Drink: ' + str(drinkItemsList[i][j]))
                elif j==2:
                    print('Price: ' + str(drinkItemsList[i][j]))
                    print('---------------------------------')

# function to prompt user to enter a drink item
def makePurchase(drinkItemsList):
    drinkChoiceID = int(input('Enter Item ID to purchase: '))
    itemExists = doesItemExists(drinkChoiceID, drinkItemsList)

# function to check whether the drink item exists
# by looping through the list to determine if the value stored in drinkChoiceID finds a match
def doesItemExists(drinkChoiceID, drinkItemsList):
    found = 0
    for i in range(len(drinkItemsList)):
        for j in range(len(drinkItemsList[i])):
            if drinkItemsList[i][j] == drinkChoiceID:
                found = 1
                makePayment(drinkItemsList[i][j + 1], drinkItemsList[i][j + 2])
    if found == 0:
        print('Drink Item ID does not exist! Try again.')

# function to handle payment of user
# 1. if user pays right amount, the selected drink will be dispensed and return to the Main Menu
# 2. if user pays insufficient amount, the user will be prompted to pay the remaining
# amount until user pays the right amount
def makePayment(drinkName, drinkPrice):
    print('\nItem to Purchase: ' + str(drinkName))
    print('Kindly pay: RM' + str(drinkPrice))
    print('\n[NOTICE] Only RM1, RM5, RM10, RM20, RM50 and RM100 notes are accepted!\n')
    price = drinkPrice
    cash = int(input('Place cash here: '))

    # input validation
    while (cash != 1 and cash != 5 and cash != 10 and cash != 20 and cash != 50 and cash != 100):
        print('[WARNING] Only RM1, RM5, RM10, RM20, RM50 and RM100 notes are accepted!')
        cash = int(input('Place cash here: '))
    remaining = price - cash
    totalPaid = cash

    # prompting the user to pay the remaining amount until user pays the right amount
    while (remaining > 0):
        print('Remaining Amount to Pay: ' + str(remaining))
        cash = int(input('Place cash here: '))

        # input validation
        while (cash != 1 and cash != 5 and cash != 10 and cash != 20 and cash != 50 and cash != 100):
            print('[WARNING] Only RM1, RM5, RM10, RM20, RM50 and RM100 notes are accepted!')
            print('Remaining Amount to Pay: ' + str(remaining))
            cash = int(input('Place cash here: '))
        remaining -= cash
        totalPaid += cash

    # calling the function to return change to user
    if (totalPaid > price):
        print('--------------------------------------------------------')
        print('Here is your change: ')
        returnChange(totalPaid, price)

    print('--------------------------------------------------------')
    print('Thank you for your purchase! Enjoy your ' + drinkName + '!')
    print('--------------------------------------------------------')

# function to process returning the smallest possible change
def returnChange(totalPaid, price):
    change = totalPaid - price
    while change > 0:
        if change >= 100:
            print('1 x RM100')
            change -= 100
        elif change >= 50:
            print('1 x RM50')
            change -= 50
        elif change >= 20:
            print('1 x RM20')
            change -= 20
        elif change >= 10:
            print('1 x RM10')
            change -= 10
        elif change >= 5:
            print('1 x RM5')
            change -= 5
        elif change >= 1:
            print('1 x RM1')
            change -= 1
    print('--------------------------------------------------------')

# function to display main menu
def mainMenu():
    drinkItemList = vendingMachineItems()
    displayItems(drinkItemList)
    while True:
        print('\nVending Machine Program')
        print('Select an operation to perform: ')
        print('1. Purchase an item')
        print('2. Exit\n')
        menuChoice = int(input('Enter operation: '))

        if menuChoice == 1:
            makePurchase(drinkItemList)
        elif menuChoice == 2:
            print('Have a nice day!')
            break
        else:
            print('Invalid input! Try again.\n')

# main program
mainMenu()