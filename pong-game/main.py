from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Pong!')
screen.tracer(0)

def main():
    game_is_on = True
    # screen.update()
    player1 = Player(1)
    player2 = Player(2)
    
    player1.create_player()
    player2.create_player()
    
    # listening for inputs
    screen.listen()
    screen.onkey(key="w", fun=player1.move_up)
    screen.onkey(key="s", fun=player1.move_down)
    screen.onkey(key="Up", fun=player2.move_up)
    screen.onkey(key="Down", fun=player2.move_down)
    
    # game is running
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        

if __name__ == '__main__':
    main()
    screen.exitonclick()