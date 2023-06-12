from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
                
        # initialising scoreboard
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER!', align='center', font=('Arial', 20, 'normal'))
        
    def update_score(self):
        self.clear()
        self.goto(-20, 260)
        self.write(arg=f'{self.score_1}', font=('Arial', 20, 'normal'))
        self.fd(40)
        self.write(arg=f'{self.score_2}', font=('Arial', 20, 'normal'))
        
