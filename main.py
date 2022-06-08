from turtle import Screen, Turtle
from food import Food
from snake import Snake
import time
from scoreboard import Scoreboard

# Ustawiamy ekran
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg='black')
screen.title('Snake')

screen.delay(delay=None)
screen.tracer(0)

snake = Snake()
food = Food()

# Ustawiamy ekran, żeby reagował na odpowiednie eventy
screen.onkeypress(snake.move_up, 'Up')
screen.onkeypress(snake.move_down, 'Down')
screen.onkeypress(snake.move_right, 'Right')
screen.onkeypress(snake.move_left, 'Left')
screen.listen()

scoreboard = Scoreboard()


game_status = True
while game_status:
    screen.update()
    time.sleep(0.05)
    scoreboard.printing_score()

    # Musimy opóźnić ponowne wykonowanie funkcji
    snake.move()

    # Zderzenie z ścianą
    if snake.head.xcor() >= 345 or snake.head.xcor() <= -365 or snake.head.ycor() >= 345 or snake.head.ycor() <= -325:
        snake.restart_position()
        snake.reset()
        scoreboard.reset()


    # Zebranie jedzenia
    if snake.head.distance(x=food.f.xcor(), y= food.f.ycor()) < 15:
        food.spawn_food()
        scoreboard.score += 1
        snake.new_segment()

    # Zderzenie z wężem
    for element in snake.elements[1:]:
        if snake.head.distance(element) < 10:
            snake.reset()
            scoreboard.reset()


screen.exitonclick()






