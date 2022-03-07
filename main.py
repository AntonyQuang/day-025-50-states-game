import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
screen.listen()
turtle.shape(image)

text = turtle.Turtle()
text.penup()
text.hideturtle()

us_states = pandas.read_csv("50_states.csv")
all_states = us_states.state.to_list()
guessed_states = []
FONT = ('Arial', 8, 'normal')

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="Name a state?").title()
while len(guessed_states) < 51:

    while answer_state in guessed_states:
        answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="You already said that "
                                                                                            "sate. What's "
                                                                                            "another state's name?").title()

    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in all_states:
        state_row = us_states[us_states["state"] == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        text.goto(x_cor, y_cor)

        text.write(answer_state, True, align="center", font=FONT)

        guessed_states.append(answer_state)

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()


