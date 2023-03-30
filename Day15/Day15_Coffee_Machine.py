MENU = {
    "espresso": {
        "ingredients": 
        {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": 
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": 
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(choice):
    # Check resources to see sufficient
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False           
    else:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        return True


def check_money(choice):
    # System money check
    quarter = int(input("Please insert coins.\nHoy many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarter * 0.25) + (dime * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total >= MENU[choice]["cost"]:
        change = total - MENU[choice]["cost"]
        return change
    else:
        return -0.1
    

money = 0
keep_working = True
##program should be in loop for every customer.
while keep_working:
    # Ask for user input
    coffee_choice = input("What would you like (espresso, latte, cappuccino): ").lower()
    if coffee_choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")
        continue
    elif coffee_choice == "off":
        keep_working = False
        continue
    enough_resource = check_resources(coffee_choice)
    if enough_resource == False:
        continue
    give_back = check_money(coffee_choice)
    if give_back < 0:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif give_back >= 0:
        print(f"Here is ${give_back} in change.")
    money += MENU[coffee_choice]["cost"]
    
    print(f"Here is your {coffee_choice}. Enjoy!")
    
    




