import turtle
import random
turtle.shape = ('square')
ghost = turtle.clone()
SQUARE_SIZE = 30
my_pos = []
ghost_pos = []

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    move_ghost()
    print('U r up!')

def left():
    global direction
    direction = LEFT
    move_ghost()
    print('U r left!')

def down():
    global direction
    direction = DOWN
    move_ghost()
    print('U r down!')

def right():
    global direction
    direction = RIGHT
    move_ghost()
    print('U r right!')

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()


def move_ghost():
    my_pos = ghost.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        ghost.goto(x_pos + SQUARE_SIZE, y_pos)
        print('R I G H T')
    elif direction == LEFT:
        ghost.goto(x_pos - SQUARE_SIZE, y_pos)
        print('L E F T')
    elif direction == UP:
        ghost.goto(x_pos, y_pos+SQUARE_SIZE)
        print('U P')
    elif direction == DOWN:
        ghost.goto(x_pos, y_pos-SQUARE_SIZE)
              


