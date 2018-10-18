#Write a program that prompts the user for a name.  The program then splits the name into first and last name (case insensitive).

#Then it:

#calls a function that returns a list of the common letters in first and last. The data structures used in this implementation can only be lists.
#calls a function that returns a set containing the common letters in first and last.  The data structures used in this implementation can only be sets.
#prints out a sorted list version of the results from 1) and 2)

def common_letters_using_list(first_name, last_name):
    common_letters = []
    for chars in last_name:
        if chars in first_name and chars not in common_letters:
            common_letters.append(chars)
    return common_letters

def common_letters_using_sets(first_name, last_name):
    common_letters = set(first_name) & set(last_name)
    return list(common_letters)


def main():
    first_name, last_name = input("Enter name: ").lower().split()  
    common_letter_list = sorted(common_letters_using_list(first_name, last_name))
    common_letter_list_2 = sorted(common_letters_using_sets(first_name, last_name))
    print(common_letter_list)
    print(common_letter_list_2)

main()