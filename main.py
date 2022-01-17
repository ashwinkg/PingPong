from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PADDLE_POS = ((400, 0), (-400, 0))

my_screen = Screen()
my_screen.screensize(canvwidth=800, canvheight=600)
my_screen.bgcolor("black")
my_screen.title("PING...PONG....")
my_screen.tracer(0)
my_screen.listen()

r_paddle = Paddle(PADDLE_POS[0])
l_paddle = Paddle(PADDLE_POS[1])
ball = Ball()
scoreboard = ScoreBoard()

my_screen.onkeypress(key="Up", fun=r_paddle.move_up)
my_screen.onkeypress(key="Down", fun=r_paddle.move_down)
my_screen.onkeypress(key="w", fun=l_paddle.move_up)
my_screen.onkeypress(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    scoreboard.print_score_board()
    ball.move_up()

    # Detecting collision with wall
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()

    # Detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 370 or ball.distance(l_paddle) < 50 and ball.xcor() < -370:
        ball.bounce_x()

    # Left player gets points
    if ball.xcor() > 400:
        scoreboard.update_left_score()
        ball.reset_ball_position()

    if ball.xcor() < -400:
        scoreboard.update_right_score()
        ball.reset_ball_position()


my_screen.exitonclick()
