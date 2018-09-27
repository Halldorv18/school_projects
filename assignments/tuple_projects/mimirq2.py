#list_to_tuple function goes here
def list_to_tuple(a_list):
    new_list =[]
    for integers in a_list:
        try:
            integers = int(integers)
        except Exception:
            print("Error. Please enter only integers.")
            return tuple()
        new_list.append(integers)
    
    return tuple(new_list)
    
# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)