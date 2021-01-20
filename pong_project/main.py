import turtle as t
from paddle import Paddle
from ball import Ball
import time as tim
from scoreboard import ScoreBoard
screen = t.Screen()
t.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# creating two paddles
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
screen.listen()
# moving right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# moving left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# creating ball
ball = Ball()
# creating scoreboard

scoreboard=ScoreBoard()
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    tim.sleep(0.1)
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("bounce")
        ball.y_bounce()

    # Detect collision with r_paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()

    # reset the game
    if ball.xcor() > 380:
        ball.home()
        ball.x_bounce()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.home()
        ball.x_bounce()
        scoreboard.r_point()







screen.exitonclick()
