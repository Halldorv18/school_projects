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

sum_of_list = 0
for number in list_contents:
    sum_of_list += number
average_of_list = sum_of_list/size

print("The average of the values in the list is: {}".format(average_of_list))