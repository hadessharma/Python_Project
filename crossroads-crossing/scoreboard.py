from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-40, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score : {self.score}')

    def game_over(self):
        self.clear()
        self.write(arg=f'Score : {self.score}')
        self.goto(0,0)
        self.write(arg=f'GAME OVER!!', font=("Arial", 20, 'normal'))