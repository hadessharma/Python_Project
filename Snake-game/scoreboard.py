from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        
        self.update_score()
        
    def update_score(self) -> None: 
        # self.score+=1
        self.clear()
        self.goto(0,280)
        self.write(arg=f'SCORE: {self.score}', move=True, align='center')
        