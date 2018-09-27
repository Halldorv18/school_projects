
def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here
value_list = get_list()
print(value_list)
user_choice = input("Enter choice (m,r): ")

if user_choice.lower() == "m":
    index_and_letter = input("")
    index_and_letter_list = index_and_letter.split(",")
    index = int(index_and_letter_list[0])
    number = int(index_and_letter_list[1])
    mutate_list(value_list, index, number)
elif user_choice.lower() == "r":
    index = int(input(""))
    remove_ch(value_list, index)
print(value_list)