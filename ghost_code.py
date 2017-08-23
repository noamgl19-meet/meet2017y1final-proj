import turtle
import random

turtle.tracer(1,0)
enemy = turtle.clone()
enemy.penup()
enemy.goto(200,0)
turtle.register_shape("ghost_F.gif")
enemy.shape("ghost_F.gif")
#enemy.shape("circle")
#screan size
SIZE_X = 1028
SIZE_Y = 800
turtle.setup(SIZE_X, SIZE_Y)
#square size
SQUARE_SIZE = 20

#installing arrows
UP_ARROW = "Up"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
LEFT_ARROW = "LEFT"
TIME_STEP = 100
#lists
pos_list = []
enemy_pos_list = []
turtle.penup()

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

direction = UP
gdirection = UP
turtle.shape("square")
def up():
    global direction
    direction = UP
    print("UP")

def down():
    global direction
    direction = DOWN

    print("DOWN")

def right():
    global direction
    direction = RIGHT

    print("RIGHT")

def left():
    global direction
    direction = LEFT
def gup():
    global gdirection
    gdirection = UP
def gdown():
    global gdirection
    gdirection = DOWN
def gleft():
    global gdirection
    gdirection = LEFT
def gright():
    global gdirection
    gdirection = RIGHT

def move_ghost():
    global TIME_STEP
    en_pos = enemy.pos()
    en_x_pos = en_pos[0]
    en_y_pos = en_pos[1]

    randNum = (random.random()) * 100
    if randNum <= 25 :
        gdirection = UP
    elif randNum >= 25 and randNum<=50:
        gdirection = DOWN

    elif randNum >= 50 and randNum<= 75:
        gdirection = RIGHT
    elif randNum >= 75:
        gdirection = LEFT
    if gdirection == UP:
        enemy.goto(en_x_pos, en_y_pos + (1.5*SQUARE_SIZE))
    if gdirection == DOWN:
        enemy.goto(en_x_pos, en_y_pos - (1.5*SQUARE_SIZE))
    if gdirection == RIGHT:
        enemy.goto(en_x_pos + (1.5*SQUARE_SIZE), en_y_pos)
    if gdirection == LEFT:
        enemy.goto(en_x_pos - (1.5*SQUARE_SIZE), en_y_pos)
        en_pos = enemy.pos()
        enemy_pos_list.append(en_pos)
    if en_x_pos >= 400 or en_x_pos <= -400:
        enemy.reset()
        enemy.penup()
    if en_y_pos >= 250 or en_y_pos <= -250:
        enemy.reset()
        enemy.penup()
    turtle.ontimer(move_ghost, TIME_STEP)
move_ghost()

turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.listen()

def move_player():
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction == RIGHT:
        turtle.goto(x_pos + (1.5*SQUARE_SIZE), y_pos)
        print("you moved to the right!")
    elif direction == LEFT:
        turtle.goto(x_pos - (1.5*SQUARE_SIZE), y_pos)
        print("you moved to the left!")
    elif direction == UP:
        turtle.goto(x_pos, y_pos + (1.5*SQUARE_SIZE))
        print("you moved UP")
    elif direction == DOWN:
        turtle.goto(x_pos, y_pos - (1.5*SQUARE_SIZE))
        print("you moved DOWN")
    my_pos = turtle.pos()
    pos_list.append(my_pos)
    print(pos_list[-1])
    global TIME_STEP
    turtle.ontimer(move_player,TIME_STEP)
    #limiting the player in the border
    if x_pos >= 400 or x_pos <= -400:
        quit()
    if y_pos >= 250 or y_pos <= -250:
        quit()
    
    if -0.1 <enemy.pos()[0] - turtle.pos()[0] < 0.1 or -0.1 < enemy.pos()[1] - turtle.pos()[1] < 0.1:
        turtle.register_shape("ghost.gif")
        enemy.shape("ghost.gif")
        if turtle.pos() in (0,0):
            
            writer.write("You Won!")
move_player()
