def is_prime(number): # is_prime function definition goes here
    prime = True
    counter = 2
    while counter < number:
        if number % counter == 0:
            prime = False
        counter +=1
    return prime

num = int(input("Input an integer greater than 1: "))
true_or_false = is_prime(num)
# Call the function here and print out the appropriate message
if true_or_false == True:
    print(num, "is a prime")
else:
    print(num, "is not a prime")