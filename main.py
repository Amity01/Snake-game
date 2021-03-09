import time
from turtle import Screen
from food import Food
from Snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(8, 25)

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
scoreboard = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -297 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        snake.erase_snake()
        scoreboard.reset()
        snake.restart()


    # detect collusion with head and body
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            snake.erase_snake()
            scoreboard.reset()
            snake.restart()



screen.exitonclick()
