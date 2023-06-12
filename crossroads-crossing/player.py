from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.reset()
        

    def reset(self):
        self.goto(0, -280)

    def move_up(self):
        self.fd(10)
