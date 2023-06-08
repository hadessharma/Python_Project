from turtle import Screen, Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.is_the_game_on = True

    def start_game(self):
        for i in range(3):
            turtle = Turtle()
            turtle.shape('square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(-i*20, 0)
            self.snake.append(turtle)

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].pos())
        self.snake[0].forward(20)

    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)


def main():
    pass


if __name__ == '__main__':
    main()


