import turtle
import time
import pygame
import random
turtle.bgcolor("black")
turtle.fillcolor("white")
#shape and turtle stuff
food = turtle.clone()
score = turtle.clone()
#setting up screan size
SIZE_X = 1280
SIZE_Y = 760
turtle.setup(SIZE_X,SIZE_Y)
score.penup()
score.ht()
score.pencolor("white")
score.goto(SIZE_X/2 - 160, SIZE_Y/2 -100)

food.shape("circle")

turtle.shape("square")
#define arrow keys
UP_ARROW = "Up"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
LEFT_ARROW = "Left"
#grid
SQUARE_SIZE = 20
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
turtle.title("noam")
turtle.penup()
direction = UP

def randfood():
    food_pos = food.pos()
    food_x_pos = food_pos[0]
    food_y_pos = food_pos[1]
    food_x = (random.random()) * 400
    food_y = (random.random()) * 300


    food.penup()
    food.goto(food_x, food_y)
randfood()
#game refresh every 100 miliseconds
TIME_STEP = 100
#functions for direction
def up():
    global direction
    direction = UP
def down():
    global direction
    direction = DOWN
def right():
    global direction
    direction = RIGHT
def left():
    global direction
    direction = LEFT
turtle.onkeypress(up, "Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
count = 0
def move_player():
    global direction, turtle, count
    #define x and y current pos
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction == UP:
        turtle.goto(x_pos,y_pos + SQUARE_SIZE)
    if direction == DOWN:
        turtle.goto(x_pos, y_pos - SQUARE_SIZE)
    if direction == RIGHT:
        turtle.goto(x_pos + SQUARE_SIZE, y_pos)
    if direction == LEFT:
        turtle.goto(x_pos - SQUARE_SIZE, y_pos)
    if -20 < food.pos()[0] - turtle.pos()[0] < 20 and -20 < food.pos()[1] - turtle.pos()[1] < 20:
        count += 1
        score.clear()

        score.write("your score is: " + str(count), font=("Ariel", 22, "normal"))
        randfood()

    turtle.ontimer(move_player, TIME_STEP)
move_player()
turtle.mainloop()
