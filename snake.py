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


def food_hunting():

    def follow_runner():
        snake_x_coord = snake.xcor()
        snake_y_coord = snake.ycor()
        if snake.heading() == 90:
            snake2.setposition(snake_x_coord, snake_y_coord-20)
        elif snake.heading() == 180:
            snake2.setposition(snake_x_coord+20, snake_y_coord)
        elif snake.heading() == 270:
            snake2.setposition(snake_x_coord, snake_y_coord+20)
        elif snake.heading() == 360:
            snake2.setposition(snake_x_coord-20, snake_y_coord)
        #snake2.setheading(snake2.towards(snake))
        snake2.forward(1)
        snake2.goto(snake_x_coord, snake_y_coord-20)
        window.ontimer(follow_runner, 50)

    snake.forward(speed)
    snake_x_coord = snake.xcor()
    snake_y_coord = snake.ycor()
    food_x_coord = food.xcor()
    food_y_coord = food.ycor()
    
    if food_x_coord-19 <= snake_x_coord <= food_x_coord+19 and food_y_coord-19 <= snake_y_coord <= food_y_coord+19:
        x = random.randint(-550, 550)
        y = random.randint(-550, 550)
        food.goto(x,y)

        snake2 = turtle.Turtle()
        snake2.speed(9)
        snake2.shape("square")
        snake2.color("red")
        snake2.penup()
        follow_runner()

def string_direction_of_snake():
    if(int(snake.heading()) == 90):
        return 'Up'
    elif(int(snake.heading()) == 180):
        return 'Left'
    elif(int(snake.heading()) == 270):
        return 'Down'
    elif(int(snake.heading()) == 0):
        return 'Right'

    
def can_go_to_direction(direction):
    print(" > " + str(direction) + " | " + str(string_direction_of_snake()) + " < ")
    return True
    return direction == string_direction_of_snake()
    #vreau sa verific in sus.
    #daca sarpele merge in sus iar eu vreau sa merg in sus, return false

    #daca directia sarpelui este directia in care vreau sa merg returnez false

def snake_up():
    if not can_go_to_direction('Up'):
        return

    snake.setheading(90)
    while True:
        food_hunting()
            
def snake_left():
    if not can_go_to_direction('Left'):
        return
    snake.setheading(180)
    while True:
        food_hunting()
    

def snake_down():
    if not can_go_to_direction('Down'):
        return
    snake.setheading(270)
    while True:
        food_hunting()

def snake_right():
    if not can_go_to_direction('Right'):
        return
    snake.setheading(360)
    while True:
       food_hunting()



# def can_go_in_direction():
#     if snake.heading() == 90:
#         window.listen()
#         window.onkeypress(snake_right, "Right")
#         window.onkeypress(snake_left, "Left")
#         window.onkeypress(snake_up, "Up")
#         window.onkeypress(None, "Down")


window.listen()
window.onkeypress(snake_right, "Right")
window.onkeypress(snake_left, "Left")
window.onkeypress(snake_up, "Up")
window.onkeypress(snake_down, "Down")





delay = input("Press Enter to finish!")