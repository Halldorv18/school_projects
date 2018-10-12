# Function definitions start here
def open_file(filename):
    try:
        file_stream = open(filename, "r")
        return file_stream
    except:
        return False
    
    
    



def get_longest_word(file_stream):
    word_list = []
    for line in file_stream:
        line = line.strip()
        word_list.append(line)
    longest_word = ""
    for words in word_list:
        if len(words) > len(longest_word):
            longest_word = words
    
        
    return longest_word

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')