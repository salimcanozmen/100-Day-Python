from turtle import Turtle
SCORE_1 = 0
SCORE_2 = 0
FONT = ("Arial", 18, "normal")


class MainScreen:
    def __init__(self):
        super().__init__()
        self.mainscreen = Turtle("square")
        self.mainscreen.color("white")
        self.mainscreen.speed("fastest")
        self.mainscreen.shapesize(stretch_len=1, stretch_wid=0.25)
        self.mainscreen.hideturtle()
        self.mainscreen.penup()
        self.mainscreen.goto(0, 360)
        self.mainscreen.right(90)
        self.mainscreen.stamp()
        while self.mainscreen.ycor() > -360:
            self.mainscreen.forward(30)
            self.mainscreen.stamp()
        self.score_1 = 0
        self.score_2 = 0
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.speed(0)
        self.score_turtle.goto(-50, 300)
        self.score_turtle.write(arg=self.score_1, font=FONT)
        self.score_turtle.goto(50, 300)
        self.score_turtle.write(arg=self.score_2, font=FONT)

    def add_score_to_1(self):
        self.score_1 += 1
        self.score_turtle.goto(-50, 300)
        self.score_turtle.clear()
        self.score_turtle.write(arg=self.score_1, font=FONT)
        self.score_turtle.goto(50, 300)
        self.score_turtle.write(arg=self.score_2, font=FONT)

    def add_score_to_2(self):
        self.score_2 += 1
        self.score_turtle.goto(50, 300)
        self.score_turtle.clear()
        self.score_turtle.write(arg=self.score_2, font=FONT)
        self.score_turtle.goto(-50, 300)
        self.score_turtle.write(arg=self.score_1, font=FONT)




