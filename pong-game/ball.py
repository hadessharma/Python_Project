from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # self.speed('slowest')
        self.penup()
        self.move()
        
    def move(self):
        self.fd(10)
    
    def bounce(self, angle):
        self.setheading(abs(180-angle))