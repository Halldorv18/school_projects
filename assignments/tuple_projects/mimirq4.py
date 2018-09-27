def get_emails():
    user_input = input("Email address: ")
    email_list = []
    while user_input.lower() != "q":
        email_list.append(user_input)
        user_input = input("Email address: ")
    return email_list
def get_names_and_domains(email_list):
    new_list = []
    for stuff in email_list:
        email_tuple = tuple(stuff.split("@"))
        new_list.append(email_tuple)
    return new_list

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)