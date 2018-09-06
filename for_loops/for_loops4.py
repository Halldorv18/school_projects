low_str = input("Input the low number: ")
low_int = int(low_str)
high_str = input("Input the high number: ")
high_int = int(high_str)
sum = 0
for number in range(low_int, high_int + 1):
    if number % 2 == 0:
        sum += number
print(sum)