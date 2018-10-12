import string

def get_word_list(fpointer):
    word_string = ""
    for line in fpointer:
        word_string += line
    word_string = word_string.strip().split()
    word_list = []
    
    for word in word_string:
        word = word.strip(string.punctuation).lower()
        word_list.append(word)
    return word_list

def word_list_to_counts(word_list):
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def dict_to_tuple(word_count_dict):
    new_list = []
    for key, val in word_count_dict.items():
        new_list.append((key, val))
    return new_list



def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()