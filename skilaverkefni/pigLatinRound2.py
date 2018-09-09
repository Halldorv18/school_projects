word = ""
vowels = "aeiouy"
pig_1 = "ay"
pig_2 = "yay"
counter = 0
while word != ".":
    word_og = input("Enter a word:")
    word = word_og.lower()
    length_of_word = len(word)
      
    if word[counter] in vowels:
        first_part = word[ 0 : (counter - 1)]
        second_part = word[counter : -1]
        pig_word = second_part + first_part + pig_1
    
    
    
    counter += 1
    print(pig_word)
