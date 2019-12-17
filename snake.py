import turtle


window = turtle.Screen()
window.title("Snakes and dots")
window.bgcolor("black")
window.setup(height=1200, width=1200)

speed = 1
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()

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
    

window.listen()
window.onkeypress(snake_up, "Up")
window.onkeypress(snake_left, "Left")



delay = input("Press Enter to finish!")