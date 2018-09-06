my_str = input("Enter a word: ")
my_syllables = "aeiouyAEIOUY"
for index, letter in enumerate(my_str):
    for index1, letter_syl in enumerate(my_syllables):
        if letter_syl == letter:
            my_new_str = my_str[index:]+ my_str[0:index]+"ay"
            break
        else:
            my_new_str = my_str + "yay"

print(my_new_str.lower())




