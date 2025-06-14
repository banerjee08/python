import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.bgcolor("black")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()





turtle.mainloop()
