from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

# move forward
def move_forward():
    tim.forward(10)

# move backward
def move_backward():
    tim.backward(10)

# move left
def move_left():
    tim.left(10)

# move right
def move_right():
    tim.right(10)

# clear screen
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()

# on click listeners
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

# exit the screen
screen.exitonclick()