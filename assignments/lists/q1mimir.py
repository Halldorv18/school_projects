import string

sentence = input("Input a sentence: ")
unique_letters = []
for letter in sentence:
    if letter.isalpha() == False:
        sentence = sentence.replace(letter, "")
    elif letter not in unique_letters:
        unique_letters.append(letter)


# Here you should add the missing part


print("Unique letters:", unique_letters)
