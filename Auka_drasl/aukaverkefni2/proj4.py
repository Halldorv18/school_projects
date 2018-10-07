import math
try:
    size = int(input("Enter the size of the list: "))
except:
    print("Invalid size, enter an int!")
    
list_contents = []
for stuff in range(0,size):
    
    try:
        list_value = int(input("Insert a value to the list: "))
    except:
        print("Invalid value, enter an int!")
        size += 1
        continue

    list_contents.append(list_value)

highest_value = -math.inf
for number in list_contents:
    if number > highest_value:
        highest_value = number
print("The highest value in the list is {}".format(highest_value))

    
    
