from turtle import Turtle, Screen

asya = Turtle()
screen = Screen()


def forward():
    asya.forward(10)


def backward():
    asya.backward(10)


def clockwise():
    asya.right(5)


def counter_clockwise():
    asya.left(5)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear, "c")

screen.exitonclick()
