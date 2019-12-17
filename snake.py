import turtle
import random


window = turtle.Screen()
window.title("Snakes and dots")
window.bgcolor("black")
window.setup(height=1200, width=1200)

speed = 1
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(-200, 0)


food = turtle.Turtle()
food.shape("square")
food.color("gray")
food.penup()
food.goto(0, 0)

# while True:
#     snake.forward(speed)

def snake_up():
    snake.setheading(90)
    while True:
        snake.forward(speed)

def snake_left():
    snake.setheading(180)
    while True:
        snake.forward(speed)

def snake_down():
    snake.setheading(270)
    while True:
        snake.forward(speed)

def snake_right():
    snake.setheading(360)
    while True:
        snake.forward(speed)
    

window.listen()
window.onkeypress(snake_up, "Up")
window.onkeypress(snake_left, "Left")
window.onkeypress(snake_down, "Down")
window.onkeypress(snake_right, "Right")




if snake.distance(food) < 20:
    x = random.randint(-550, 550)
    y = random.randint(-550, 550)
    food.goto(x,y)

delay = input("Press Enter to finish!")