import string

def get_file_name():
    file_name = input("Document collection: ")
    print("")
    return file_name

def get_file_contents(file_name):
    with open(file_name, "r") as file_contents:
        file_contents_str = ""
        for line in file_contents:
            file_contents_str += line
    return file_contents_str

def list_of_words_in_document(document_list):
    clean_document_list = []
    for documents in document_list:
        list_of_words_in_doc = documents.split()
        temp_list = []
        for word in list_of_words_in_doc:
            for letter in word:
                word = word.replace("\n", "")
                if letter in string.punctuation:
                    word = word.replace(letter, "")
            temp_list.append(word.lower())
        clean_document_list.append(temp_list)
    
    return clean_document_list
            
def make_document_list(file_contents):
    document_list = file_contents.split("<NEW DOCUMENT>\n")
    returning_document_list = document_list[1:]
    return returning_document_list

def instructions():
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")

def get_input_from_user():
    choice = int(input(""))
    return choice

def operations(clean_list, document_list):
    while True:
        instructions()
        choice = get_input_from_user()
        index_of_search_words = set()
        if choice == 1:
            search_words = input("Enter search words: ").lower()
            search_words = search_words.split()
            for document in clean_list:
                for word in search_words:
                    if word in document:
                        index_of_search_words.add(clean_list.index(document))
                        
            print("Documents that fit search:", end = " ")
                
            for number_of_doc in index_of_search_words:
                print(number_of_doc, end = " ")


        elif choice == 2:
            doc_index = int(input("Enter document number: "))
            document_to_print =  "".join(document_list[doc_index])
            print("{} {}".format("Document", "#" + str(doc_index)))
            print(document_to_print)
        else:
            break
        print("")

def main():
    file_name = get_file_name()
    file_contents = get_file_contents(file_name)
    document_list = make_document_list(file_contents)
    clean_list = list_of_words_in_document(document_list)
    operations(clean_list, document_list)


main()