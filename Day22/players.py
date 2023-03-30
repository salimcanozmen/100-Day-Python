from turtle import Turtle
STARTING_POS = [(-620, 0), (620, 0)]


class Player:

    def __init__(self):
        self.players = []
        self.create_players()
        self.player1 = self.players[0]
        self.player2 = self.players[-1]

    def create_players(self):
        for i in STARTING_POS:
            segment = Turtle("square")
            segment.speed(0)
            segment.penup()
            segment.hideturtle()
            segment.color("white")
            segment.goto(i)
            segment.seth(90)
            segment.shapesize(stretch_len=4)
            segment.showturtle()
            self.players.append(segment)

    def player1_up(self):
        if self.player1.ycor() > 300:
            return
        self.player1.forward(20)

    def player1_down(self):
        if self.player1.ycor() < -300:
            return
        self.player1.backward(20)

    def player2_up(self):
        if self.player2.ycor() > 300:
            return
        self.player2.forward(20)

    def player2_down(self):
        if self.player2.ycor() < -300:
            return
        self.player2.backward(20)
