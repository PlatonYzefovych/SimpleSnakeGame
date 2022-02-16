from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


def the_game():
    # Starting setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    '''Imported classes'''
    snake = Snake()
    food = Food()
    score = Score()

    '''Keys bindings'''
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    '''While loop for game running and finishing. "update()" uses for no clipping on screen'''
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        '''Detect collision with food'''
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        '''Detect collision with the walls'''
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()

        '''Detect collision with tail'''
        # if head collides with any segment in the tail:
        # trigger game_over
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()



    screen.exitonclick()


the_game()
