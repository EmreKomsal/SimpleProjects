from turtle import Screen, Turtle
from snake import Snake, Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Snake setup
snake = Snake()

game_is_on = True

food = Food()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    
    time.sleep(0.2)
    
    if snake.check_food_collision(food):
        snake.add_segment()
        food.refresh()
        scoreboard.increase_score()
        

    if snake.check_screen_collision() or snake.check_collision():
        snake.reset()
        scoreboard.reset()
        scoreboard.game_over()
    
    scoreboard.update_scoreboard()
    
    snake.move()
    
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    
    
    
screen.exitonclick()

