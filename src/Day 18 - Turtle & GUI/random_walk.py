import turtle
import random
from colors import random_color

timmy = turtle.Turtle()

screen = turtle.Screen()
screen.colormode(255)

# Set width and speed
timmy.width(18)
timmy.speed(0)

# Do random walk
angles = [0, 90, 180, 270]
for _ in range(200):
    timmy.color(random_color())
    timmy.fd(50)
    timmy.lt(random.choice(angles))

screen.exitonclick()
