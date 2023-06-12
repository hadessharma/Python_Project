from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time
import random

def game(screen, score) -> None:
    game_is_on = True

    cars = [Cars('Red', i*30) for i in range(10)]
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        f = random.randint(1, 10)
        for i in range(f):
            cars[i].move_cars()
            
        pass    

def main():
    
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title('Crossing!')
    screen.tracer(0)
    
    player = Player()
    score  = Scoreboard()

    # listening for player movement
    screen.listen()
    screen.onkey(key="Up", fun=player.move_up)
    
    # game function
    game(screen, score)

    # exit the screen on click
    screen.exitonclick()
if __name__=='__main__':
    main()