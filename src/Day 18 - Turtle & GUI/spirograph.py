import turtle
from colors import random_color

timmy = turtle.Turtle()

screen = turtle.Screen()
screen.colormode(255)

# Set width and speed
timmy.width(1)
timmy.speed(0)

num_of_circles = 30

for _ in range(num_of_circles):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.lt(360 / num_of_circles)

screen.exitonclick()
