import turtle
import pandas

IMAGE = './map-game/blank_states_img.gif'

screen = turtle.Screen()
screen.title('U.S. State Game!!')
screen.addshape(IMAGE)

turtle.shape(IMAGE)

score = 0

game_is_on = True

state_data = pandas.read_csv('./map-game/50_states.csv')

# sam is for writing 
sam = turtle.Turtle()
sam.hideturtle()
sam.penup()

# toby is for writing the missed answer
toby = turtle.Turtle()
toby.hideturtle()
toby.penup()
toby.color('red')
# state_data.loc[state_data['state'] == 'Florida', 'x'].item()


while game_is_on:
    
    answer_state = screen.textinput(title=f'{score}/50 left!', prompt='Type the state name:').title()
    
    if answer_state == 'Exit':
        # Give all the missing answers in RED
        for state in state_data['state'].to_list():
            toby.goto(state_data.loc[state_data['state'] == f'{state}', 'x'].item(), state_data.loc[state_data['state'] == f'{state}', 'y'].item())
            toby.write(arg=f'{state}')
        
        # Exit game 
        game_is_on = False

    if answer_state in state_data['state'].tolist():
        score += 1
        sam.goto(state_data.loc[state_data['state'] == f'{answer_state}', 'x'].item(), state_data.loc[state_data['state'] == f'{answer_state}', 'y'].item())
        sam.write(arg=answer_state)
        state_data = state_data.drop(index = [row for row in state_data.index if f'{answer_state}' in state_data.loc[row].values])
        

turtle.mainloop()
