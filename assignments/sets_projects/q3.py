#Write a program that reads in a file and prints out the 10 most frequent bigrams in the file.  A bigram is a sequence of two adjacent words.

#Note that you should use a dictionary (not a set) in this project, because you need to keep track of the counts of each bigram (thus a key-value pair).

#Further instructions:

#all words need to be converted to lower case
#all words need to be stripped of punctuations
#The keys in the bigram dictionary should be tuples (word1, word2)
#The values are the occurences of the given bigram in the text
#Dictonaries are unordered collections. You can however, transform a dictionary to a list of tuples (using the items() method) and then sort it.  Look at itemgetter on pages 355-356 in the textbook.
import string
def get_text_from_file(filename):
    with open(filename, "r") as file_contents:
        file_contents_str = ""
        for line in file_contents:
            for word in line:
                word = word.strip(string.punctuation).lower()
                file_contents_str += word  
    file_contents_str = file_contents_str.strip(string.punctuation)    
    file_contents_str = file_contents_str.replace("\n", " ")                       #file_contents.remove(string.punctuation)
    return file_contents_str

def convert_str_to_list(string):
    my_list = string.split()
    return my_list

def make_list_of_tuples(my_list):
    list_of_tuples = []
    for index, letter in enumerate(my_list):
        if index == len(my_list) - 1 :
            break
        list_of_tuples.append((letter, my_list[index + 1 ]))
    return list_of_tuples

def count_tuple_frequency(tuple_list):
    my_list = []
    for elements in tuple_list:
        my_list.append((elements, tuple_list.count(elements)))
    my_list = list(set(my_list))
    return my_list

def top_10(counting_list):
    counter = 10
    top_10_list = []
    #while counter < 0 :
          
        #top_10_list.append(max(counting_list))
        
        
        
def main(): 
    filename = input("Enter name of file: ")
    text = get_text_from_file(filename)
    my_list = convert_str_to_list(text)
    tuples = make_list_of_tuples(my_list)
    frequency = count_tuple_frequency(tuples)
    print(frequency)



main()