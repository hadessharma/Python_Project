from turtle import Turtle

START_POSITION = [20, 0, -20]
LENGTH_OF_BOARD = 3

class Player(Turtle):
    def __init__(self, playerpos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.playerpos = playerpos
        
    def create_player(self):
        # for i in range(LENGTH_OF_BOARD):
        #     turtle = Turtle()    
        #     turtle.color('white')
        #     turtle.shape('square')
        #     turtle.penup()
        if self.playerpos == 1:
            self.goto(-280, 0)
        else:
            self.goto(280, 0)
            # self.board.append(turtle)
    
    # movement functions     
    def move_up(self):
        self.sety(self.ycor()+20)
    
    def move_down(self):
        self.sety(self.ycor()-20)
            
    