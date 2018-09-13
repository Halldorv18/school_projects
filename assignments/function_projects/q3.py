def between_1_and_555(number):# The function definition goes here
    if 1 < number < 555:
        number = str(number)+ " is in range."
    else:
        number = str(number) + " is outside the range!"
    return  number

num = int(input("Enter a number: "))

print(between_1_and_555(num))# You call the function here