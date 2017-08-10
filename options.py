import turtle

def option():
    #turtle.clear()
    turtle.bgcolor("black")
    turtle.bgpic("box.gif")
    turtle.penup()
    turtle.ht()
    turtle.pencolor("white")
    turtle.goto(-300,1280/2-500)
    turtle.write("press b to go back to main menu! \n to move, use your arrows.\n to pause the game(5 seconds), press p.", font = ("Ariel", 20, "normal"))
    turtle.goto(-300,1280/2-730)
    turtle.write("The single player:\n you need to grab the food from the ghost, \n and after go to the village. \n each watermelon that you will deliever, \n gaining you 100 points. if you will have less \n then 0 points, you lose!", font = ("Ariel", 20, "normal"))
    turtle.goto(-300,1280/2-910)
    turtle.write("Multiplayer: \n in the multiplayer, \n the ghost needs to catch the player. \n if the ghost catches the player, \n she wins.", font = ("Ariel", 20, "normal"))

    def back():
        turtle.clear()
        import showcase
    turtle.onkeypress(back, "b")
    turtle.onkeypress(back, "B")
    turtle.listen()
