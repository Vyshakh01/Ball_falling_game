from turtle import Turtle
import random
colors=["red","blue","yellow","orange","green","purple"]

class Balls():
    def __init__(self):
        super().__init__()
        self.Balls=[]
#        self.increment=20
        self.create_balls()
    def create_balls(self):
        if random.randint(1,7)==1:
            ball=Turtle()
            ball.shape("circle")
            ball.penup()
            ball.goto(random.randint(-250,250),300)
            ball.color(random.choice(colors))
            ball.setheading(270)
            self.Balls.append(ball)
    def move(self):
        for ball in self.Balls:
            increment=20
            ball.forward(increment)
            #if ball.ycor()<-290:
            #    ball.setheading(90)




    
    
            