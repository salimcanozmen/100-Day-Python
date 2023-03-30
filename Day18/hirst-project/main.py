import colorgram
import turtle as t
import random
from turtle import Screen

colors = colorgram.extract("image.jpg" , 25)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tuple1 = (r, g, b)
    rgb_colors.append(tuple1)

t.colormode(255)
asya = t.Turtle()
asya.speed(0)
asya.hideturtle()
asya.penup()
x = -300
y = -300
asya.goto(x, y)
asya.pendown()

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
              (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (166, 204, 202), (62, 26, 45),
              (145, 165, 181), (6, 79, 111)]


#sol alt köşeye pozisyon fixle
for _ in range(10):
    for i in range(10):
        asya.color(random.choice(color_list))
        asya.begin_fill()
        asya.circle(20)
        asya.end_fill()
        asya.penup()
        asya.forward(50)
    y += 50
    asya.goto(x, y)


screen = Screen()
screen.exitonclick()





