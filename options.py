import turtle
turtle.penup()
turtle.ht()
turtle.goto(-25,1280/2-500)
turtle.write("to move, use your arrows.\n to pause the game(5 seconds), press p.")
turtle.goto(-25,1280/2-600)
turtle.write("to get back, press b or B")
def back():
    turtle.clear()
    import mainMenu
turtle.onkeypress(back, "b")
turtle.onkeypress(back, "B")
turtle.listen()
