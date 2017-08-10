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
    def mode2():
        turtle.clear()
        import ghost2p
        ghost2p.move_player()
        ghost2p.move_ghost()
    turtle.onkeypress(start, "s")
    turtle.onkeypress(start, "S")
    turtle.onkeypress(options, "o")
    turtle.onkeypress(options, "O")
    turtle.onkeypress(mode2,"m")
    turtle.onkeypress(mode2,"M")

    turtle.listen()
   
mainMenu()
