from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=650, width=650)
screen.title("Snake Game")
screen.tracer(0)

yilan = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(yilan.up, "w")
screen.onkeypress(yilan.down, "s")
screen.onkeypress(yilan.right, "d")
screen.onkeypress(yilan.left, "a")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)
    yilan.move()
    if yilan.head_snake.distance(food) < 18:
        food.spawn_food(yilan.segments)
        scoreboard.add_score()
        yilan.new_snake_part()

    if yilan.head_snake.xcor() >= 325 or yilan.head_snake.xcor() <= -325 or yilan.head_snake.ycor() >= 325 or yilan.head_snake.ycor() <= -325:
        scoreboard.game_over()
        game_on = False

    for i in yilan.segments[1:]:
        if yilan.head_snake.distance(i) < 1:
            scoreboard.game_over()
            game_on = False





screen.exitonclick()
