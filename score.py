from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.balls_missed=0
        self.goto(-0,250)
        self.hideturtle()
        self.pencolor("white")
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"SCORE :{self.score}",align="center",font=("Courrier",24,"normal"))

    def point(self):
        self.score+=1
        self.update_score()
    def lose(self):
       self.balls_missed += 1

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courrier", 24, "normal"))
#       self.update_score()


