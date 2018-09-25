import string
def to_list(string):
    better_string = string.replace(",", " ")
    my_output = better_string.split()

    
    return my_output


        
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)