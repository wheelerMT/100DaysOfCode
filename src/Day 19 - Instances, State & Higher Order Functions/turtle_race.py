import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the "
                                                         "race? Enter a color: ")

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for turtle_index in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle_list.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turt in turtle_list:
        turt.fd(random.randint(0, 10))
        if turt.xcor() > 230:
            winning_turtle = turt.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle is the winner!")
                is_race_on = False
                break
            else:
                print(f"You lost! The {winning_turtle} turtle is the winner!")
                is_race_on = False
                break


screen.exitonclick()
