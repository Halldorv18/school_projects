my_word = ""
vowels = "aeiouyAEIOUY"
pig_1= "yay"
pig_2 = "ay"
counter = 0 
while my_word != ".":
    my_word = input("Enter a word: ")
    for index, letter in enumerate(my_word):
        syllable = my_word.find(letter)
        if len(my_word) == 3 and my_word[index] in vowels:
            first_part = my_word[ 0 : (syllable)]
            second_part = my_word[1:]
            new_word = second_part + first_part + pig_2
        elif letter in vowels and index != 0:
            first_part = my_word[ 0 : syllable]
            second_part = my_word[syllable : ]
            new_word = second_part + first_part + pig_2
            
        elif my_word[0] in vowels:
            new_word = my_word + pig_1
            
        elif index == (len(my_word) - 1) and my_word[-1] not in vowels:
            new_word = my_word + pig_2
 
        else:
            new_word = my_word
            continue
        if my_word == ".":
            quit
        else:
            print(new_word)
            break


        
