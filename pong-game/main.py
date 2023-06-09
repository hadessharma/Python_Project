from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Pong!')
screen.tracer(0)

def main():
    game_is_on = True
    player1 = Player(1)
    player2 = Player(2)
    screen.update()
    screen.exitonclick()

if __name__ == '__main__':
    main()