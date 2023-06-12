from turtle import Turtle
import random

COLOR = 'red'

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.level = 1
        self.penup()
        self.hideturtle()
        self.create_cars()

    def create_cars(self):
        for i in range(-10, 10, 1):
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(COLOR)
            car.goto(280, i*20)
            car.setheading(180)
            # adding to the list of cars
            self.cars.append(car)

    def move_cars(self):
        rate = random.randint(1, 19)
        for i in range(rate):
            self.cars[i].fd(10*self.level)
            if self.cars[i].xcor() < -280:
                self.cars[i].setx(280)
