my_word = input("Enter a word: ")
vowels = "aeiouyAEIOUY"
pig_1= "yay"
pig_2 = "ay"

    
for index, letter in enumerate(my_word):
    if my_word.find(".") >= 0:
        quit()
    elif letter in vowels and index != 0:
        syllable = my_word.find(letter)
        first_part = my_word[ 0 : syllable]
        second_part = my_word[syllable: - 1]
        new_word = second_part + first_part + pig_2
        break
    elif my_word[0] in vowels:
        new_word = my_word + pig_1
        break
    else:
        new_word = my_word
     
print(new_word)
