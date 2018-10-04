def merge_lists(list1, list2):
    new_list = []
    other_list = []
    for obj in list1:
        new_list.append(obj)
    for obj in list2:
        new_list.append(obj)
    new_list.sort()
    for thing in new_list:
        if thing not in other_list:
            other_list.append(thing)
    return other_list

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
