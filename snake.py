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
snake.speed(0)


food = turtle.Turtle()
food.shape("square")
food.color("gray")
food.penup()
food.goto(0, 0)
food.speed(0)



def snake_up():
    
    def follow_runner():
        snake2.setposition(snake_x_coord, snake_y_coord-20)
        snake2.setheading(snake2.towards(snake))
        snake2.forward(1)
        window.ontimer(follow_runner, 1)

    snake.setheading(90)
    while True:
        snake.forward(speed)
        snake_x_coord = snake.xcor()
        snake_y_coord = snake.ycor()
        print(snake_x_coord, snake_y_coord)
        food_x_coord = food.xcor()
        food_y_coord = food.ycor()
        
        if food_x_coord-19 <= snake_x_coord <= food_x_coord+19 and food_y_coord-19 <= snake_y_coord <= food_y_coord+19:
            x = random.randint(-550, 550)
            y = random.randint(-550, 550)
            food.goto(x,y)

            snake2 = turtle.Turtle()
            snake2.speed(0)
            snake2.shape("square")
            snake2.color("red")
            snake2.penup()
            follow_runner()
            
            
def snake_left():
    def follow_runner():
        snake2.setposition(snake_x_coord+20, snake_y_coord)
        snake2.setheading(snake2.towards(snake))
        snake2.forward(1)
        window.ontimer(follow_runner, 10)

    snake.setheading(180)
    while True:
        snake.forward(speed)
        snake_x_coord = snake.xcor()
        snake_y_coord = snake.ycor()
        print(snake_x_coord, snake_y_coord)
        food_x_coord = food.xcor()
        food_y_coord = food.ycor()
        
        if food_x_coord-19 <= snake_x_coord <= food_x_coord+19 and food_y_coord-19 <= snake_y_coord <= food_y_coord+19:
            x = random.randint(-550, 550)
            y = random.randint(-550, 550)
            food.goto(x,y)

            snake2 = turtle.Turtle()
            snake2.speed(0)
            snake2.shape("square")
            snake2.color("red")
            snake2.penup()
            follow_runner()
    

def snake_down():
    def follow_runner():
        snake2.setposition(snake_x_coord, snake_y_coord+20)
        snake2.setheading(snake2.towards(snake))
        snake2.forward(1)
        window.ontimer(follow_runner, 100)

    snake.setheading(270)
    while True:
        snake.forward(speed)
        snake_x_coord = snake.xcor()
        snake_y_coord = snake.ycor()
        print(snake_x_coord, snake_y_coord)
        food_x_coord = food.xcor()
        food_y_coord = food.ycor()
        
        if food_x_coord-19 <= snake_x_coord <= food_x_coord+19 and food_y_coord-19 <= snake_y_coord <= food_y_coord+19:
            x = random.randint(-550, 550)
            y = random.randint(-550, 550)
            food.goto(x,y)

            snake2 = turtle.Turtle()
            snake2.speed(0)
            snake2.shape("square")
            snake2.color("red")
            snake2.penup()
            follow_runner()

def snake_right():
    def follow_runner():
        snake2.setposition(snake_x_coord-20, snake_y_coord)
        snake2.setheading(snake2.towards(snake))
        snake2.forward(1)
        window.ontimer(follow_runner, 10)

    snake.setheading(360)
    while True:
        snake.forward(speed)
        snake_x_coord = snake.xcor()
        snake_y_coord = snake.ycor()
        print(snake_x_coord, snake_y_coord)
        food_x_coord = food.xcor()
        food_y_coord = food.ycor()
        
        if food_x_coord-19 <= snake_x_coord <= food_x_coord+19 and food_y_coord-19 <= snake_y_coord <= food_y_coord+19:
            x = random.randint(-550, 550)
            y = random.randint(-550, 550)
            food.goto(x,y)

            snake2 = turtle.Turtle()
            snake2.speed(0)
            snake2.shape("square")
            snake2.color("red")
            snake2.penup()
            follow_runner()


    

window.listen()
window.onkeypress(snake_up, "Up")
window.onkeypress(snake_left, "Left")
window.onkeypress(snake_down, "Down")
window.onkeypress(snake_right, "Right")






delay = input("Press Enter to finish!")