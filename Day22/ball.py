import random
from turtle import Turtle
BALL_SPEED = 10
OPTIONS = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.penup()
        self.starter_x = random.choice(OPTIONS)
        self.starter_y = random.choice(OPTIONS)

    def move_ball(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + self.starter_x, current_y + self.starter_y)

    def refresh(self):
        self.hideturtle()
        self.speed(0)
        self.goto(0, 0)
        self.starter_y *= -1
        self.starter_x *= -1
        self.speed(1)
        self.showturtle()
        return False



