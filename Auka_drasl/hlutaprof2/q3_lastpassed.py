def split_string(user_input):
    main_list = user_input.split(",")
    return main_list

def make_sublists(a_list):
    list_size = len(a_list)
    returning_list = []
    for index, stak in enumerate(a_list):
        if index == 0:
            temp_list = []
        else:
            temp_list = [stak]
            index += 1
        for number in range(index, list_size):
            temp_tuple = tuple(temp_list.append(a_list[number])
        returning_list.append(list(temp_tuple))
    returning_list.insert(0, [])
    return returning_list
        


        


# Main program starts here
user_input = input("Enter a list separated with commas: ")
main_list = split_string(user_input)
sub_lists = make_sublists(main_list)
# This should be the last statement in your main program/function 
print(sorted(sub_lists))
