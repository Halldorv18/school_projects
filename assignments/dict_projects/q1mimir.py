def get_input():
    name = input("Name: ")
    phone_number = input("Number: ")
    return name, phone_number

def add_contact_to_phone_book(phone_book, name, number):
    phone_book[name] = number

def change_to_tuple_list(phone_book):
    tuple_list = []
    for name, value in phone_book.items():
        tuple_list.append((name, value))
    return tuple_list

def main():
    phone_book = {}
    choice = "y"
    while choice == "y":
        name, number = get_input()
        add_contact_to_phone_book(phone_book, name, number)
        choice = input("More data (y/n)? ")
    phone_book_list = change_to_tuple_list(phone_book)
    print(sorted(phone_book_list))

    

main()