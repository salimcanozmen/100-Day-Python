import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=800)
game_on = False
winner_choice = screen.textinput(title="Make a bet", prompt="Who is going to win the race?")
colour = ["Blue", "Purple", "Green", "Red", "Orange", "Yellow"]
race_pos = 100
all_turtles = []
for i in range(0, 6):
    asya = Turtle(shape="turtle")
    asya.color(colour[i])
    asya.penup()
    asya.goto(-250, race_pos)
    race_pos -= 50
    all_turtles.append(asya)

if winner_choice:
    game_on = True

while game_on:
    for i in all_turtles:
        move = random.randint(1, 10)
        i.forward(move)
        if i.xcor() > 280:
            winner = i
            renk = winner.pencolor()
            game_on = False
if winner_choice.lower() == renk.lower():
    print("You won!")
else:
    print("You lost.")
print(f"Winner is {renk}")
screen.exitonclick()

