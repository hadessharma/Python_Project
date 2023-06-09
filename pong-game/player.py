from turtle import Turtle

START_POSITION = [20, 0, -20]
LENGTH_OF_BOARD = 3

class Player(Turtle):
    def __init__(self, playerpos):
        self.board = []
        self.playerpos = playerpos
        
    def create_player(self):
        for i in range(LENGTH_OF_BOARD):
            turtle = Turtle()    
            turtle.color('white')
            turtle.shape('square')
            turtle.penup()
            if self.playerpos == 1:
                turtle.goto(-280, START_POSITION[i])
            else:
                turtle.goto(280, START_POSITION[i])
            self.board.append(turtle)
    
    # movement functions     
    def move_up(self):
        for segment in self.board:
            segment.sety(segment.ycor()+20)
    
    def move_down(self):
        for segment in self.board:
            segment.sety(segment.ycor()-20)
            
    