def split_string(user_input):
    if type(user_input) == type([2,3]):
        main_list = user_input
    else:
        main_list = user_input.split(",")
    
    return main_list

def make_sublists(a_list):
    sub_list = []
    size_of = len(a_list)
    for index, thing in enumerate(a_list):
        if index == 0:
            sub_list.append(list(thing))
        else:
            for index1 in range(0,index + 1  ):
                sub_list.append(a_list[index1 :index + 1 ])

    
    sub_list.insert(0, [])
    return sub_list
    
# Main program starts here
user_input = input("Enter a list separated with commas: ")
main_list = split_string(user_input)
sub_lists = make_sublists(main_list)
# This should be the last statement in your main program/function 
print(sorted(sub_lists))
