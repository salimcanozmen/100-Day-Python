from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu1 = Menu()
coffeemaker = CoffeeMaker()
moneyy = MoneyMachine()

while True:
    user_choice = input(f"What would you like? ({menu1.get_items()}): ")
    if user_choice == "off":
        exit()
    if user_choice == "report":
        coffeemaker.report()
        moneyy.report()
        continue
    selected_coffee = menu1.find_drink(user_choice)
    if coffeemaker.is_resource_sufficient(selected_coffee) and moneyy.make_payment(selected_coffee.cost):
        coffeemaker.make_coffee(selected_coffee)