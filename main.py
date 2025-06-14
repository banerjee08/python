import turtle, pandas

from numpy.matlib import empty

# importing states data
states_data = pandas.read_csv(r"50_states.csv")
all_state = states_data["state"].to_list()
# print(states_data)

# Keeping an universal count
count = 0
guessed_states = []
missed_states = []

# setting up the screen
screen = turtle.Screen()
screen.bgcolor("black")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while count < 50:
    screen.title(f"U.S. States Game - {count} States guessed!")

    # Getting input from the turtle
    answer_state = screen.textinput(
        title=f"Guess another state",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        break

    if answer_state.title() == "Exit":
        for state in all_state:
            if state not in guessed_states:
                missed_states.append(state)

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        print(missed_states)

    answer_state = answer_state.title()
    if answer_state in all_state and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        count += 1

        valid_name = states_data[states_data["state"] == answer_state]
        print(valid_name)
        # Getting the values
        state_name = valid_name["state"]
        x_cord = int(valid_name["x"])
        y_cord = int(valid_name["y"])

        # Writing the name of the state on the map
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x_cord, y_cord)
        writer.write(f"{answer_state}", align="center", font=("Arial", 12, "normal"))

turtle.mainloop()
