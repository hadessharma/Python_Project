from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        # self.goto(random.randint(-280,280), random.randint(-280, 280))
        self.reset_food()
        
    def reset_food(self) -> None:
        self.goto(random.randint(-280, 280), random.randint(-280,280))
    
    