turn_int = int(input("How often do you want to input an integer?: "))
counter = 0
negetive_int = 0
while counter <= turn_int:
    num_int = int(input("Please enter an integer: "))
    if num_int < 0:
        negetive_int += 1
        print(negetive_int)
    counter +=1