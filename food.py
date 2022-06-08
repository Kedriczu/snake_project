from turtle import Turtle
import random

class Food():
    def __init__(self):
        self.f = Turtle()
        self.f.shape("circle")
        self.f.color('orange')
        self.f.pu()
        self.f.speed('fastest')
        self.f.goto(100, y=100)
        self.f.shapesize(0.5, 0.5, 0.5)


    def spawn_food(self):
        self.f.goto(x=random.randint(-300,300), y=random.randint(-300,300))