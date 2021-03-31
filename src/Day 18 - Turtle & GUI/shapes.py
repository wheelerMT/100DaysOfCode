import turtle

timmy = turtle.Turtle()

# Gen color list
colors = ["blue", "DeepPink", "chocolate", "gold", "green", "LightCoral", "RoyalBlue", "red"]

# Gen a num of side list
sides = [3, 4, 5, 6, 7, 8, 9, 10]

timmy.width(4)
for num_of_sides in sides:
    timmy.color(colors[sides.index(num_of_sides)])
    for i in range(num_of_sides):
        timmy.rt(360 / num_of_sides)
        timmy.fd(100)
screen = turtle.Screen()
screen.exitonclick()