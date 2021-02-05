

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



#TODO: 3. Create function that will print out main message “What would you like? (espresso/latte/cappuccino):”
def menuSelection():
    userSelection = ""
    userSelection.lower()

# TODO: 1. Create a while loop that will execute while a coffee machine is 'on'”
    while (userSelection != "off"):
        userSelection = input("What would you like? (espresso/latte/cappuccino)\n")

        # TODO: 2. Print a report of all the coffee resources
        if(userSelection == "report"):
            for element in resources:
                print(element + ": " + str(resources[element]))
                print(f"Profit:0 ${profit}")
        elif(userSelection == "espresso"):
            if(checkResources("espresso") == True):
                checkout("espresso")
        elif (userSelection == "latte"):
            if (checkResources("latte") == True):
                generateEspresso()
        else:
            print("I am so sorry! I don't think we actually have that drink :(")


def checkout(drink):
    global profit

    costOfDrink = (MENU[drink]["cost"])
    currentAmount = 0
    Coins = {'Quarters': .25, 'dimes': .10, 'Nickles': .05, 'Pennies': .01}


    print("Nice, " + drink + " is my personal favorite!! " + "That will be: $" + str(costOfDrink))


    for element in Coins:
        userInput = input(f"How many {element} would you like to use (use integers)?")
        currentAmount += int(userInput) * Coins.get(element)
        print("Remaining total: " + str(costOfDrink - currentAmount))


    if currentAmount < costOfDrink:
        print("I am so sorry! It appears you are " + str(costOfDrink) + " short")
    else:
        if currentAmount > costOfDrink:
            print("Yea!! Here is your change $" + str(costOfDrink * -1) )

        print("Enjoy☕!!")
        profit += (MENU[drink]["cost"])


#TODO: 4. Check resources to see if you have enough to make drinks
def checkResources(drink):

    #=====================================================
    # Acquire the amount of resources that will
    # remain once the current drinks requirements
    # have been deducted. This will aid in determining
    # if we have enough to make the drink
    #======================================================
    futureWaterAmount = resources["water"] - MENU[drink]["ingredients"]["water"]
    futureCoffeeAmount = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    depletedResources = ""

    if(drink != "espresso"):
        futureMilkAmount = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    else:
        futureMilkAmount = 0

    # =====================================================
    # Identify what resources are depleted and prompt user
    # ======================================================
    if futureCoffeeAmount <= 0:
        depletedResources = "Coffee"
    if futureWaterAmount <= 0:
        if depletedResources != "":
            depletedResources += ",Water"
        else:
            depletedResources += "Water"
    if futureMilkAmount and drink != "espresso" <= 0:
        if depletedResources != "":
            depletedResources += ",Milk"
        else:
            depletedResources += "Milk"
    if depletedResources != "":
        print("I am so sorry! It appears we are low on " + depletedResources)
        return False

    # =====================================================
    # Deduct the resources used to make coffee
    # ======================================================
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


    return True





# =====================================================
# Kick off program
# ======================================================

print("Let's Rock!")
menuSelection()





