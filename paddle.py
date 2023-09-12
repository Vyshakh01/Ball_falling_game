from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0,-200)
        self.color("white")
        self.shapesize(stretch_len=2)
        self.setheading(0)
        self.color("red")
    def right(self):
        self.forward(20)
    def left(self):
        self.backward(20)
