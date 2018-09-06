high_str = input("Input a number: ")
high_int = int(high_str)
low_str = input("Input another number: ")
low_int = int(low_str)
for number in range(low_int, high_int):
    if number % 2 != 0:
        print(number)