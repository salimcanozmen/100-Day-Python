import pandas
import turtle
from cevap import Cevap

screen = turtle.Screen()
cevap = Cevap()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_list = states["state"].to_list()
game_on = True
correctly_answered = []
while game_on:
    answer = screen.textinput(title=f"{len(correctly_answered)}/50 Guess the State", prompt="Guess a states name")
    answer = answer.title()
    if answer == "Exit":
        # list_of_states_to_learn = []
        list_of_states_to_learn = [to_learn for to_learn in state_list if to_learn not in correctly_answered]
        states_to_learn = {
            "States to Learn": list_of_states_to_learn
        }
        ## Old version of code before learning list comprehension.
        # for to_learn in state_list:
        #     if to_learn not in correctly_answered:
        #         list_of_states_to_learn.append(to_learn)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States to Learn.csv")
        break
    if answer not in correctly_answered:       
        for state in state_list:
            if answer == state:
                row_info = states[states.state == answer]
                x_cor = int(row_info.x)
                y_cor = int(row_info.y)
                cevap.write_answer(x=x_cor, y=y_cor, prompt=answer)
                correctly_answered.append(answer)
    if len(correctly_answered) == 50:
        print("Well done. You are a True American.")
        game_on = False


    
