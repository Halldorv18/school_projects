import random
import string
def get_word_string(filename):
    try:
        with open(filename, "r") as dataFile:
            word_list = []
            for line in dataFile:
                line = line.strip() 
                word_list.append(line)
            
            word_string = " ".join(word_list)
        return word_string
    except:
        print("File {} not found".format(filename))
        return ""
def scrambled_string(word_string):
    if word_string == "":
        return ""
    word_list = word_string.split(" ")
    outcome_str = ""
    for word in word_list:
        word = str(word)
        last_letters = word[-1]
        middle_list = list(word[1:-1])
        if word[-1] in string.punctuation:
            middle_list = list(word[1: -2])
            last_letters = word[-2:]
        random.shuffle(middle_list)    
        first_letter = word[0]
        scrambled_middle = "".join(middle_list)
        new_string = first_letter + scrambled_middle + last_letters
        if len(word) == 1:
            new_string = str(word)
    
        outcome_str += str(new_string) + " "
    return outcome_str
# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scrambled_string(word_string)
print(scrambled_string)
