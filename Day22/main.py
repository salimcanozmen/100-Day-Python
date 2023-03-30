from turtle import Turtle, Screen
from players import Player
from main_screen import MainScreen
from ball import Ball
import time

screen = Screen()
screen.setup(width=1280, height=720)
screen.bgcolor("black")
screen.tracer(0)

main = MainScreen()
players = Player()
ball = Ball()

screen.listen()
screen.onkeypress(players.player1_up, "w")
screen.onkeypress(players.player1_down, "s")
screen.onkeypress(players.player2_up, "Up")
screen.onkeypress(players.player2_down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.02)
    ball.move_ball()
    if ball.ycor() >= 340:
        ball.starter_y = -10
    elif ball.ycor() <= -340:
        ball.starter_y = 10
    elif ball.distance(players.player1) <= 50 and ball.xcor() < -590:
        ball.starter_x = 10
    elif ball.distance(players.player2) <= 50 and ball.xcor() > 590:
        ball.starter_x = -10
    elif ball.xcor() > 640:
        ball.refresh()
        main.add_score_to_1()
    elif ball.xcor() < -640:
        ball.refresh()
        main.add_score_to_2()



