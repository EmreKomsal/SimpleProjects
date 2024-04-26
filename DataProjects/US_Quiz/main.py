import turtle
import pandas as pd
from scoreboard import Scoreboard

# Set up the screen
def setup_screen():
    screen = turtle.Screen()
    screen.title("US States Game")
    image = "PythonProjects/SimpleProjects/DataProjects/US_Quiz/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    return screen

def get_mouse_click_coor(x, y):
    print(x, y)
    
def ask_state(screen, score):
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    return answer_state
    
def read_data():
    data = pd.read_csv("PythonProjects/SimpleProjects/DataProjects/US_Quiz/50_states.csv")
    return data

def check_state(data, state):
    return data[data.state == state]

def write_state_screen(state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(state['x'].values[0]), int(state['y'].values[0]))
    t.write(state['state'].values[0])
    
    
def main():
    screen = setup_screen()
    #turtle.onscreenclick(get_mouse_click_coor)
    #turtle.listen()
    user_score = 0
    user_input = ""
    data = read_data()
    user_states = []
    scoreboard = Scoreboard()
    while user_input != "Exit":
        user_input = ask_state(screen, user_score)
        if user_input == "Exit":
            scoreboard.game_over()
            break
        if user_input in user_states:
            continue
        state = check_state(data, user_input)
        if not state.empty:
            user_score += 1
            scoreboard.increase_score()
            user_states.append(state.state.values[0])
            write_state_screen(state)
            scoreboard.update_scoreboard()
    turtle.mainloop()
    
if __name__ == "__main__":
    main()