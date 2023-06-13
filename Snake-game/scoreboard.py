from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = 0 
        self.color('white')
        self.penup()
        self.hideturtle()       

        # check for highscore
        with open("./Python_Project/Snake-game/highscore.txt", mode="w+") as highscore:
            self.highscore = highscore.read()
            if self.highscore == '':
                self.highscore = 0
        
        self.update_score()


    def update_score(self) -> None: 
        # self.score+=1
        self.clear()
        self.goto(0,280)
        self.write(arg=f'SCORE: {self.score}   High Score: {self.highscore}', align='center')
        
    def reset(self):
        self.clear()
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("./Python_Project/Snake-game/highscore.txt", mode="w") as highscore:
                highscore.write(str(self.highscore))

        self.score = 0
        self.write(arg=f'SCORE: {self.score}   High Score: {self.highscore}', align='center')   
                