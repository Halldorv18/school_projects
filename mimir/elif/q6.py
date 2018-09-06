d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: "))
dice_sum = d1 + d2
if 1 <= d1 <= 6 and 1 <= d2 <= 6:
    if dice_sum == 7 or dice_sum == 11:
        print("Winner")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print("Loser")
    else:
        print(dice_sum)
else:
    print("Invalid input")
    