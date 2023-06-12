from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time
import random

def game(screen, score, player) -> None:
    game_is_on = True

    cars = Cars()
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        f = random.randint(1, 10)
        
        # if player crosses finish line
        if player.ycor() > 270:
            player.reset()
            # update score
            score.score += 1
            score.update_score()
            cars.level += 1

        # move the cars continuosly    
        cars.move_cars()

        # check for collsions
        for car in cars.cars:
            if car.distance(player) < 25:
                score.game_over()
                game_is_on = False

            

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
    game(screen, score, player)

    # exit the screen on click
    screen.exitonclick()
if __name__=='__main__':
    main()