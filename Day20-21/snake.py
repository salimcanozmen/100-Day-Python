from turtle import Turtle, Screen
screen = Screen()
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head_snake = self.segments[0]

    def create_snake(self):
        for start_pos in STARTING_POS:
            snake_part = Turtle("square")
            snake_part.penup()
            snake_part.speed("slowest")
            snake_part.color("white")
            snake_part.goto(start_pos)
            self.segments.append(snake_part)

    def new_snake_part(self):
        snake_part = Turtle("square")
        snake_part.hideturtle()
        snake_part.penup()
        snake_part.speed("fastest")
        snake_part.color("white")
        x = self.segments[len(self.segments) - 1].xcor()
        y = self.segments[len(self.segments) - 1].ycor()
        snake_part.goto(x, y)
        snake_part.speed("slowest")
        snake_part.showturtle()
        self.segments.append(snake_part)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_snake.heading() == 270.0:
            return
        self.head_snake.seth(90)
        self.move()

    def down(self):
        if self.head_snake.heading() == 90.0:
            return
        self.head_snake.seth(270)
        self.move()

    def right(self):
        if self.head_snake.heading() == 180.0:
            return
        self.head_snake.seth(0)
        self.move()

    def left(self):
        if self.head_snake.heading() == 0.0:
            return
        self.head_snake.seth(180)
        self.move()



