size_str = input("Input the list size ")
size_int = int(size_str)
numbers = []
sum_of_list = 0
for x in range(size_int):
    number_str = input("Pick a number ")
    number_int = int(number_str)
    sum_of_list += number_int
    numbers.append(number_int)
print("The average of the numbers chosen is: ", sum_of_list / size_int)