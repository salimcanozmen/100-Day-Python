from turtle import Turtle


class Cevap(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_answer(self, x, y, prompt):
        self.goto(x, y)
        self.write(arg=prompt, move=True, align='center')
        