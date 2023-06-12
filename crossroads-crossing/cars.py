from turtle import Turtle

class Cars(Turtle):
    def __init__(self, colour, pos):
        super().__init__()
        self.level = 1
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.color(colour)
        self.goto(280, pos)

    def move_cars(self):
        self.setheading(180)
        self.fd(10*self.level)