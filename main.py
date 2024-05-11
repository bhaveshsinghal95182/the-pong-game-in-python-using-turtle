from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.screensize(800,600,"black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()