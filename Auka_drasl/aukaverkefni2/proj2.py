size = int(input("Enter the size of the list: "))
list_contents = []
for stuff in range(0,size):
    list_value = input("Insert a value to the list: ")
    list_contents.append(list_value)
target = input("Enter a value: ")
if target in list_contents:
    print("{} is in the list.".format(target))
else:
    print("{} is not in the list.".format(target))



    