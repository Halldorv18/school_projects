size = int(input("Enter the size of the list: "))
list_contents = []
for stuff in range(0,size):
    list_value = input("Insert a value to the list: ")
    list_contents.append(list_value)
target = input("Enter a value: ")
target_counter = 0
for index, letter in enumerate(list_contents):
    if target not in list_contents:
        print("Target value not in list!")
    elif target == letter:
        target_counter += 1
if target_counter != 0:
    print("Value {} occurs {} times in the list.".format(target, target_counter))
    

    



    