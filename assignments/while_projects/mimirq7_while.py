count = 1


while count <= 18:
    par = int(input("Par of hole {0}: ".format(count)))
    score = int(input("Score on hole {0}: ".format(count)))
    if score - par == 0:
        print ("par")
    elif score - par == 1:
        print ("bogey")
    elif score - par == 2:
        print ("double bogey")
    elif score - par == 3:
        print ("triple bogey")
    elif par - score == 1:
        print ("birdie")
    elif par - score == 2:
        print ("eagle")
    elif par - score == 3:
        print ("albatross")
    elif score - par > 3:
        print ("bad hole")
    elif par - score > 3:
        print ("invalid score")
    count = count + 1