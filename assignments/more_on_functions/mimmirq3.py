import string

#build_wordlist() function goes here
def build_wordlist(infile):
    outcome_str = ""
    for line in infile:
        outcome_str += line
    outcome_str = outcome_str.replace("\n", " ")
    outcome_list = outcome_str.split(" ")
    return outcome_list

        
    
        

#find_unique() function goes here
def find_unique(word_list):
    other_list =[] 
    for stuff in word_list:
        if stuff not in other_list:
            other_list.append(stuff)
    return other_list

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()
