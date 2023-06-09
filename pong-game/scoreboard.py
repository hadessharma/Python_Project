from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER!', align='center')