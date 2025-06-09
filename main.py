from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
# tim.penup()
# colors of the turtle
colors=["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
is_race_on = False
all_turtles = []

screen = Screen()

# setting up the screen
screen.setup(width=500, height=400)

# Getting input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# setting the initial point of the turtle
# tim.goto(x=-238, y=-100)

# Setting y coordinate
y_cord = -100

# creating multiple turtles
for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-238, y=y_cord)
    all_turtles.append(new_turtle)
    y_cord += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for each_turtle in all_turtles:
        if each_turtle.xcor() > 220:
            winning_color = each_turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You won!!! The {winning_color} coloured turtle won!")
            else:
                print(f"You lost!!! The {winning_color} coloured turtle won!")
        random_distance = random.randint(0,10)
        each_turtle.forward(random_distance)


# exit screen
screen.exitonclick()