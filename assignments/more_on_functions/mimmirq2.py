#sort_list() function goes here
def sort_list(a_list):
    a_list.sort()

def main():
    #loop to accept integers until a non-digit is entered goes here
    user_input = "1"
    
    string_list = []
    while user_input.isdigit() == True:
        user_input = input("")
        string_list.append(user_input)
    
    string_list.pop()
    
    a_list = [int(x) for x in string_list]    
    
            
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()