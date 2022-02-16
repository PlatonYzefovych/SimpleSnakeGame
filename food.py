from turtle import Turtle
import random

'''Creates food on random position by inheriting from turtle classes'''


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
        self.refresh()

    '''Refreshes food position when snake hits it '''

    def refresh(self):
        random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
