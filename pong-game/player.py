from turtle import Turtle
START_POSITION = [20, 0, -20]

class Player(Turtle):
    def __init__(self, playerpos):
        self.board = []
        self.playerpos = playerpos
        self.create_player()
        
    def create_player(self):
        for i in range(3):
            turtle = Turtle()    
            turtle.color('white')
            turtle.shape('square')
            turtle.penup()
            if self.playerpos == 1:
                turtle.goto(-280, START_POSITION[i])
            else:
                turtle.goto(280, START_POSITION[i])
            self.board.append(turtle)
        