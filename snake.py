import turtle

#Screen 

window = turtle.Screen()
window.title("Snakes and dots")
window.bgcolor("black")
window.setup(height=600, width=800)
window.tracer(0)



#Snake

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(-300, 0)
#Food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("gray")
food.penup()
food.goto(0, 0)

#Snake Movement

def snake_up():
    # y = snake.ycor()
    # y += 20
    # snake.sety(y)
    while True:
        snake.forward(1)
    
def snake_down():
    y = snake.ycor()
    y -= 20
    snake.sety(y)
    snake.dy = 2

def snake_right():
    x = snake.xcor()
    x += 20
    snake.setx(x)
    snake.dx = 2

def snake_left():
    x = snake.xcor()
    x -= 20
    snake.setx(x)
    snake.dx = 2


    

#Key Bindings
window.listen()
window.onkeypress(snake_up, "Up")
window.onkeypress(snake_down, "Down")
window.onkeypress(snake_left, "Left")
window.onkeypress(snake_right, "Right")

while True:
    window.update()
    if snake.ycor() > 290:
        snake.goto(-300, 0)
    if snake.ycor() < -290:
        snake.goto(-300, 0)
    if snake.xcor() > 390:
        snake.goto(-300, 0)
    if snake.xcor() < -390:
        snake.goto(-300, 0)


    #if (snake.xcor() == food.xcor) and (snake.ycor == food.ycor):

    

  






