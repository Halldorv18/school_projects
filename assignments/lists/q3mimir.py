# Your functions should appear here
def triple_list(a_list):
    outcome = a_list * 3
    return outcome
def populate_list(a_list):
    check = True
    while check == True:
        user_input = input("Enter value to be added to list: ")
        if user_input.lower() == "exit":
            check = False
        else:
            a_list.append(user_input)
    return a_list
       
        
        
# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
