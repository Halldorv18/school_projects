my_str = input("Enter a sentence: ")

upper_case = 0
lower_case = 0
digits = 0
punctuation = 0
for index, letter in enumerate(my_str):
    if letter.isupper() == True:
        upper_case += 1
    elif letter.islower() == True:
        lower_case += 1
    elif letter == " ":
        continue
    elif letter.isdigit() == True:
        digits += 1
    else:
        punctuation += 1
    
print('{:>15}''{:>5}'.format("Upper case",upper_case))
print('{:>15}''{:>5}'.format("Lower case",lower_case))
print('{:>15}''{:>5}'.format("Digits",digits))
print('{:>15}''{:>5}'.format("Punctuation",punctuation))



