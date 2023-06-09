from turtle import Screen, Turtle

UP    = 90
DOWN  = 270
LEFT  = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []

    def start_game(self):
        for i in range(3):
            turtle = Turtle()
            turtle.shape('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(-i*20, 0)
            self.snake.append(turtle)

    def grow(self):
        turtle = Turtle()
        turtle.shape('square')
        turtle.penup()
        
        if self.snake[-1].heading() == UP:
            turtle.goto(self.snake[-1].xcor(), self.snake[0].ycor()-20)        
        if self.snake[-1].heading() == DOWN:
            turtle.goto(self.snake[-1].xcor(), self.snake[0].ycor()+20)        
        if self.snake[-1].heading() == LEFT:
            turtle.goto(self.snake[-1].xcor()+20, self.snake[0].ycor())        
        if self.snake[-1].heading() == UP:
            turtle.goto(self.snake[-1].xcor()-20, self.snake[0].ycor())  
         
        turtle.color('white')    
        self.snake.append(turtle)  
                
    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].pos())
        self.snake[0].forward(20)

    def move_up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def move_down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def move_left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def move_right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)


def main():
    pass


if __name__ == '__main__':
    main()


