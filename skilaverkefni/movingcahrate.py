def instructions(x):
    print("l - for moving left")
    print("r - for moving right")
    print("Another other letter for quitting")
def position_change(x):
    while 1 < x < 10 and str(x).isdigit() == True:
        instructions(0)
        movement = input("Input your choice: ")
        movement = l_or_r(x, movement)
        print("New position is: ", movement)
        x = movement
    else:
        print("Invalid input!")
def l_or_r(number,x):
    if x == "r":
        movement = number + 1
    elif x == "l":
        movement = number - 1
    return movement
position = int(input("Input a position between 1 and 10: "))
position_change(position)

    


    

