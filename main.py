import turtle
import pandas
from tkinter import messagebox


screen=turtle.Screen()
screen.title("U.S. state")
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()

for i in range (50):
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state count?").title()
    print(answer_state)
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    if i>50:
        messagebox.showinfo("Done", "You have guessed all 50 state")

#use for the screen open

