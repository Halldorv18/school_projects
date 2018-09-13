def count_case(x):# Your function definition goes here
    lower = 0
    upper = 0
    for letter in user_input:
        if letter.isupper() == True:
            upper +=1
        elif letter.islower() == True:
            lower += 1
    return upper, lower


user_input = input("Enter a string: ")
upper, lower = count_case(user_input)
# Call the function here

print("Upper case count: ", upper)
print("Lower case count: ", lower)