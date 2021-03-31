import colorgram
import turtle
import random


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

timmy = turtle.Turtle()
timmy.speed(0)

# Set initial turtle position
timmy.pu()
timmy.setx(-250)
timmy.sety(-250)

screen = turtle.Screen()
screen.colormode(255)

num_of_rows = 10

# Paint Hirst painting
turtle.begin_fill()
for row in range(num_of_rows):
    for _ in range(10):
        timmy.color(random.choice(rgb_colors))
        timmy.dot(20)
        timmy.pu()
        timmy.fd(50)
        timmy.pd()
    timmy.pu()
    timmy.setx(-250)
    timmy.sety(-250 + (row + 1) * 50)
    timmy.pd()

screen.exitonclick()
