# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("orange")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
x = dict()
x = table.add_column("Pokemon name", ["Pikachu", "Squirtle"])
y = table.add_column("Pokemen type", ["Electric", "Water"])
table.align = "l"

print(table)

