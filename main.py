import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data['state'].tolist()
score = 0

writer = Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")
game_exit = "Exit"

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?").title()
    if answer_state in states:
        print(answer_state)
        hold_data = data[data.state == answer_state]
        new_x = int(hold_data.iloc[0]['x'])
        new_y = int(hold_data.iloc[0]['y'])
        score += 1
        writer.goto(new_x, new_y)
        writer.write(f"{answer_state}", align="center", font="Courier")
        print(hold_data)
        print(new_x)
        print(new_y)
    elif answer_state == game_exit:
        game_is_on = False


