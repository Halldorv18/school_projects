size = int(input("Insert list size "))
numbers = []
sum_of_list = 0
for number in range(size):
    number_str = input("Input a number ")
    number_int = int(number_str)
    sum_of_list += number_int
    numbers.append(number_int)
print("Loop finished, sum is: ", sum_of_list)