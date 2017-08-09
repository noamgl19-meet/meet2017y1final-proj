def mainMenu():
    import turtle
    def start():
        import ghost
        ghost.turtle.clear()
        
          
        ghost.move_ghost() 
        
        ghost.move_player()
        print("asd")
    def options():
        turtle.clear()

        import options
    turtle.penup()
    turtle.goto(-50,1280/2-500)
    turtle.write("to start press Y or y!", font=(28))
    turtle.goto(-50,1280/2-550)
    turtle.write("to option screan, press O or o", font=(28))
    turtle.onkeypress(start, "Y")
    turtle.onkeypress(start, "y")
    turtle.onkeypress(options, "o")
    turtle.onkeypress(options, "O")
    turtle.listen()
   
mainMenu()
