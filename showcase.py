def mainMenu():
    import turtle
    SIZE_X = 1280
    SIZE_Y = 720
    turtle.setup(SIZE_X, SIZE_Y)
    turtle.bgcolor("black")
    turtle.bgpic("bg_main_menu.gif")
    def start():
        import ghost
        ghost.turtle.clear() 
        ghost.move_ghost()     
        ghost.move_player()
        print("asd")
    def ops():
        turtle.clear()
        import options
        options.option()
    def mode2():
        turtle.clear()
        import ghost2p
        ghost2p.move_player()
        ghost2p.move_ghost()
    turtle.onkeypress(start, "s")
    turtle.onkeypress(start, "S")
    turtle.onkeypress(ops, "o")
    turtle.onkeypress(ops, "O")
    turtle.onkeypress(mode2,"m")
    turtle.onkeypress(mode2,"M")
    turtle.listen()
   
mainMenu()
