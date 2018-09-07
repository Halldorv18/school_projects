my_str = input("Enter a word: ")
my_syllables = "aeiouyAEIOUY"
for index, letter in enumerate(my_str):
    for index1, letter_syl in enumerate(my_syllables):
        if letter_syl == letter:
            first_split = my_str[:index]+"ay"
            second_split = my_str[index:]
            my_new_str = second_split + first_split
        else:
            my_new_str = my_str + "yay"
        break

print(my_new_str.lower())



print(first_split)
print(second_split)
