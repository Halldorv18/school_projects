
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

def transform(list1, list2, index1, index2):
    #list2.append(list1[index1 : index2])
    new_list = []
    int_index1 = int(index1)
    int_index2 = int(index2) 
   
    new_list.append(list1[int_index1:int_index2:-1])
    for stuff in list1:
        if stuff in new_list:
            list1.remove(stuff)
    
        
        #if int_index1 <= index <= int_index2:
         #   if index == (int_index1 + 1):
          #      int_index2 -= 1
           #list1.remove(stuff)
            
    
    

    
    return new_list



# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)