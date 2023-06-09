from turtle import Screen
from player import Player
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Pong!')
screen.tracer(0)

def main():
    game_is_on = True
    player1 = Player(1)
    player2 = Player(2)
    ball = Ball()
    scoreboard = Scoreboard()
    
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
        ball.move()
        
        for i in range(3):
            if player1.board[i].distance(ball) < 15 or player2.board[i].distance(ball) < 15:
                ball.bounce(ball.heading())
        
        if ball.xcor() >= 290 or ball.xcor() <= -290 or ball.ycor() <= -290 or ball.ycor() >= 290:    
            game_is_on = False
            scoreboard.game_over()

if __name__ == '__main__':
    main()
    screen.exitonclick()