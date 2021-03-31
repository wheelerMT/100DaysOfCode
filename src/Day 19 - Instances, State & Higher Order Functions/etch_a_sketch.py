import turtle


def move_forward():
    timmy.fd(20)


def move_backward():
    timmy.bk(20)


def turn_left():
    timmy.lt(20)


def turn_right():
    timmy.rt(20)


def clear():
    # screen.clear()
    screen.reset()


timmy = turtle.Turtle()

screen = turtle.Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
