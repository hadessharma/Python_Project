from turtle import Turtle

class Ball(Turtle):
    def __init__(self, xdir, ydir):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # self.speed('slowest')
        self.penup()
        self.xdir = xdir
        self.ydir = ydir
        self.move()
        
    def move(self):
        self.goto(self.xcor() + self.xdir*10, self.ycor() + self.ydir*10)
    
    def bounce(self):
        self.goto(self.xcor() + self.xdir*10 , self.ycor() + self.ydir*10)