from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.start_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.write(f"Score: {self.start_score}", False, align="center")

    def add_score(self):
        self.start_score += 1
        self.clear()
        self.write(f"Score: {self.start_score}", False, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")
