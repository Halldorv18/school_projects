def instructions(x):
    print("l - for moving left")
    print("r - for moving right")
    print("Another other letter for quitting")
def position_change(x):
    while 1 < x < 10 and str(x).isdigit() == True:
        instructions(0)
        movement = input("Input your choice: ")
        if movement == "l":
            movement = x - 1
        elif movement == "r":
            movement = x + 1
        print("New position is: ", movement)
        x = movement
    else:
        print("Invalid input!")

position = int(input("Input a position between 1 and 10: "))
position_change(position)

    


    

