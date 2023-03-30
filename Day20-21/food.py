from turtle import Turtle, Screen
from snake import Snake
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        self.goto(x, y)

    def spawn_food(self, pos_info):
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        self.goto(x, y)
        good_food = False
        while not good_food:
            reset = 0
            for i in pos_info:
                if self.distance(i) < 18:
                    x = random.randrange(-300, 300)
                    y = random.randrange(-300, 300)
                    self.goto(x, y)
                    reset = 1
            if reset == 0:
                break



