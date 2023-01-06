from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My first Video Game In Python, SNAKE!")
# animation positions
screen.tracer(0)
# object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# head hace referencia al cuadrado unicail de la culebra


screen.listen()
# moving -> sensible
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_in_on = True
# for each segment contain a part of snake
while game_in_on:
    # uptdate image screenw
    screen.update()
    # define time reload iamge screen
    time.sleep(0.1)
    snake.move()
    # Detect collision -> food
    # position -> comparar distancia entre dos tortugas
    if snake.head.distance(food) < 15:  # simplemente la firferencia que hay entre uno y otro
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # dtection collision wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_in_on = False
        scoreboard.game_over()

    # with tail -> fas faicl indicar desde donde a donde debe ir segun la posicion que ty le indiques asi no se molesta ocn la cabeza
    for segment in snake.segments[1:]: # this code retor a new list
        if snake.head.distance(segment) < 10:
            game_in_on = False
            scoreboard.game_over()

screen.exitonclick()
