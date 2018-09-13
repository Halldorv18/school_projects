m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line
if n > m:
    first_number = n
elif n == m:
    print("Invalid input!")
else:
    first_number = m

for num in range(2, first_number):
    if m % num == 0 and n % num == 0:
        lowest_dude = num
print(lowest_dude)