low_str = input("Enter the lower number: ")
low_int = int(low_str)
high_str = input("Enter the higher number: ")
high_int = int(high_str)
sum = 0
for number in range(low_int, high_int):
    sum += number
print(sum)