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
        if food.distance(snake.snake[0]) < 15:
            scoreboard.score += 1
            snake.grow()
            scoreboard.update_score()
            food.reset_food()
        snake.move()
        # Detect collison with wall
        if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280: 
            scoreboard.game_over()
            game_is_on = False
            
        # Detect collion with the tail
        for segment in snake.snake[1:]:
            if snake.snake[0].distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False
        

if __name__ == '__main__':
    main()
    screen.exitonclick()
