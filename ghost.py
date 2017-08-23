import random
import time
import turtle
import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.play(-1)

turtle.tracer(1,0)
enemy = turtle.clone()
enemy.st()
enemy.penup()
enemy.goto(200,-100)
turtle.register_shape("ghost_F.gif")
enemy.shape("ghost_F.gif")
does_player_have_food= False

vil_pos = []
vill_tup = (400,400)
vil_pos.append(vill_tup)

#enemy.shape("circle")
#screan size
SIZE_X = 1280
SIZE_Y = 720
turtle.setup(SIZE_X, SIZE_Y)
#square size
SQUARE_SIZE = 20
#doing the borders
def draw_box():
    box = turtle.clone()
    #disign box
    turtle.bgpic("forest.png")
    box.pencolor("green")
    box.penup()
    box.goto(SIZE_X/2, SIZE_Y/2)
    box.pendown()
    box.goto(SIZE_X/2,-SIZE_Y/2)
    box.goto(-SIZE_X/2, -SIZE_Y/2)
    box.goto(-SIZE_X/2, SIZE_Y/2)
draw_box()
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
scores = []

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

direction = UP
gdirection = UP
turtle.register_shape("player.gif")
turtle.shape("player.gif")
score = turtle.clone()
score.hideturtle()
score.goto(SIZE_X/2-250, SIZE_Y/2 - 100)
score.pencolor("white")
score.write("score: " ,font=("Arial", 28, "normal"))
count = 0
village = turtle.clone()
turtle.register_shape("village.gif")
village.shape("village.gif")
village.penup()
village.ht()
randNum1 = (random.random()) * 100
randNum2 = (random.random()) * 100
if randNum1 <= 100:
    randNum1 = (random.random()) * 100
if randNum2 <= 100:
    randNum2 = (random.random()) * 100



village.goto(-400,-300)
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
    if en_x_pos >= SIZE_X/2:
        enemy.ht()
        enemy.goto(-SIZE_X/2-2, en_y_pos)
        enemy.showturtle()

    elif en_x_pos <= -SIZE_X/2:
        enemy.ht()
        enemy.goto(SIZE_X/2-2, en_y_pos)
        enemy.showturtle()

    elif en_y_pos >= SIZE_Y/2:
        enemy.ht()
        enemy.goto(en_x_pos, -SIZE_Y/2-2)
        enemy.showturtle()

    elif en_y_pos <= -SIZE_Y/2:
        enemy.ht()
        enemy.goto(en_x_pos, SIZE_Y/2-2)
        enemy.showturtle()
    turtle.ontimer(move_ghost, TIME_STEP)

turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.listen()
if_player_food = False

def move_player():
    global village, if_player_food
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction == RIGHT:
        turtle.goto(x_pos + (1.5*SQUARE_SIZE), y_pos)
        #print("you moved to the right!")
    elif direction == LEFT:
        turtle.goto(x_pos - (1.5*SQUARE_SIZE), y_pos)
        #print("you moved to the left!")
    elif direction == UP:
        turtle.goto(x_pos, y_pos + (1.5*SQUARE_SIZE))
        #print("you moved UP")
    elif direction == DOWN:
        turtle.goto(x_pos, y_pos - (1.5*SQUARE_SIZE))
        #print("you moved DOWN")
    my_pos = turtle.pos()
    pos_list.append(my_pos)
    #print(pos_list[-1])
    global TIME_STEP
    global count
        
    #limiting the player in the border
    if x_pos > SIZE_X/2:
        turtle.ht()
        turtle.goto(-SIZE_X/2 + 10, y_pos)
        turtle.st()
    elif x_pos <= -SIZE_X/2:
        turtle.ht()
        turtle.goto(SIZE_X/2, y_pos)
        turtle.st()

    elif y_pos > SIZE_Y/2:
        turtle.ht()
        turtle.goto(x_pos, -SIZE_Y/2+2)
        turtle.st()

    elif y_pos <= -SIZE_Y/2:
        turtle.ht()
        turtle.goto(x_pos, SIZE_Y/2-2)
        turtle.st()
    if -30 <enemy.pos()[0] - turtle.pos()[0] < 30 and -30 < enemy.pos()[1] - turtle.pos()[1] < 30:
        turtle.register_shape("ghost.gif")
        enemy.shape("ghost.gif")
        turtle.register_shape("player_F.gif")
        turtle.shape("player_F.gif")
        

        village.st()
        
        enemy.goto(0,0)
        
        
            

        ## Try to understand me!!!???        
        if_player_food = True
    if (-15 <village.pos()[0] - turtle.pos()[0] < 15 and -15 < village.pos()[1] - turtle.pos()[1] < 15):
        
        if if_player_food == True:

            



            score.clear()
            count +=100
            scores.append(count)
            score.pencolor("white")
            score.write("score: "+str(count),font=("Arial", 28, "normal"))
            
        enemy.shape("ghost_F.gif")
        turtle.shape("player.gif")
        if_player_food == False
    
    if count == 1000:
        turtle.goto(0,0)
        turtle.pencolor("white")
        turtle.write("PLayer won!", font = ("Ariel", 28,"normal"))
        time.sleep(5)
        quit()
        



    turtle.ontimer(move_player,TIME_STEP)


def going_menu():
    time.sleep(5)
turtle.onkeypress(going_menu, "p")
turtle.listen()
 
        

