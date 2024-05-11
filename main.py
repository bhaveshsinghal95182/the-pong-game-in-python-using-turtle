from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(800,600,"black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
s_left = Scoreboard((-200, 250))
s_right = Scoreboard((200, 250))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.x_move += 1
        ball.y_move += 1

    if ball.xcor() > 380:
        s_left.increase_score()
        ball.ball_reset()

    if ball.xcor() < -380:
        s_right.increase_score()
        ball.ball_reset()

screen.exitonclick()