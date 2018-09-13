def palindrome(sentence):# palindrome function definition goes here
    result = ""
    for letter in sentence:
        if letter.isalpha():
            result += letter
    return result.lower()

in_str = input("Enter a string: ")
x = palindrome(in_str)
y = palindrome(in_str)[::-1]
if x == y:
    print('"' + in_str + '"', "is a palindrome.")
else:
    print('"'+in_str+'"', "is not a palindrome.")  


# call the function and print out the appropriate message