def instructions(x): #Prints out instructions for position movement
    """
    Prints out instructions for the user
    """
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

def one_and_ten(x, movement): #Prevents the user to move the point outside the [1, 10] range
    """
    Keeps the position within the [1, 10] range
    """
    if (x == 1 and movement == "l") or (x == 10 and movement == "r"):
        return True

def exit_input(movement, x): #If the user inputs a letter that isnt "r" or "l" it prints out the last position and quits

    if movement.isalpha() == True and movement != "l" and movement != "r":
        print("New position is:", x)
        return True

def position_change(x): #Determines the new postition in accordance with the user input
    """
    Determines the new postition in accordance with the user input
    """
    while str(x).isdigit() == True:
        instructions(0)
        movement = input("Input your choice: ")
        if exit_input(movement, x) == True:
            break
        if one_and_ten(x, movement) == True:
            print("New position is:", x)
            continue
        elif movement == "l":
            movement = x - 1
        elif movement == "r":
            movement = x + 1
        x1 = x
        x = movement
        
        print("New position is:", x)
    else:
        print("New postion is:", x1)
    return True



position = int(input("Input a position between 1 and 10: "))
position_change(position)

    


    

