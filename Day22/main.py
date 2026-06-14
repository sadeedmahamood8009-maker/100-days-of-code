from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
sc = Screen()
sc.setup(height=600, width=800)
sc.bgcolor("black")
sc.title("pong")

sc.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scboard = ScoreBoard()

sc.listen()
sc.onkey(r_paddle.go_up, 'Up')
sc.onkey(r_paddle.go_down, 'Down')
sc.onkey(l_paddle.go_up, 'w')
sc.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320:
        ball.x_bounce()

    if ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.x_bounce()
    
    if ball.xcor() > 380:
        ball.reset_ball()
        scboard.l_joint()

    if ball.xcor() < -380:
        ball.reset_ball()
        scboard.r_joint()

sc.exitonclick()