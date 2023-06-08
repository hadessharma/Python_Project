import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game!')
screen.tracer(0)

def main():
    snake = Snake()
    food  = Food()
    scoreboard = Scoreboard()
    
    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)
    snake.start_game()
    
    
    game_is_on = True
    
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if food.distance(snake.snake[0]) < 15:
            scoreboard.update_score
            food.reset_food()


if __name__ == '__main__':
    main()
    screen.exitonclick()
