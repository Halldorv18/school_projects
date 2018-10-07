try:
    size = int(input("Enter the size of the list: "))
except:
    print("Invalid size, enter an int!")
the_list = []
counter = 1
for stuff in range(0, size):
    value = input("value no. {}: ".format(counter))
    the_list.append(value)
    counter += 1
print("The list: {}".format(the_list))
no_dup_list = []
for stuff in the_list:
    if stuff not in no_dup_list:
        no_dup_list.append(stuff)
print("The list with no duplicates: {}".format(no_dup_list))



