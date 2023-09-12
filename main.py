import turtle
from paddle import Paddle
from balls import Balls
import time
from score import Scoreboard
screen=turtle.Screen()
screen.setup(700,600)
screen.bgcolor("black")
screen.title("BALL_FALLING")
screen.tracer(0)

paddle=Paddle()
balls=Balls()
scoreboard=Scoreboard()
screen.listen()
screen.onkeypress(fun=paddle.right,key="Right")
screen.onkeypress(fun=paddle.left,key="Left")
is_game_on=True
while is_game_on:
   screen.update()
   time.sleep(0.07)
   balls.create_balls()
   balls.move()
   for ball in balls.Balls:
      if paddle.distance(ball)<20:
         ball.goto(1200,1200)
         scoreboard.point()
      if ball.ycor() < -280:
         scoreboard.lose()
      if scoreboard.balls_missed>5000 :
         is_game_on=False
         scoreboard.gameover()


#   balls.bounce()



screen.exitonclick()