#game_of_eights() function goes here
def game_of_eights(number_list):
    try:
        for i in number_list:
            int(i)     
    except:
        print("Error. Please enter only integers.")
        return ""

    for index, number in enumerate(number_list):
        
        try:
            if number == "8" and number_list[index+1] == "8":
                return True
        except:
            return False

   
    
    return False
    
def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    print(game_of_eights(a_list))
    
main()