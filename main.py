from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Objects of class(Turtle/=>Paddle/Ball/Scoreboard)
r_paddle = Paddle((350, 0)) # (350=.xcor(),0=.ycor())=>[.goto(position) in paddle.py]
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    
    ball.move()

    #Detect collision with wall(ceiling and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x_r_paddle()

    #Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and (-330 > ball.xcor() > -355):
        ball.bounce_x_l_paddle()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()