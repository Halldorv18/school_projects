string1 = ""
for number in range(1, 11):
    for number1 in range(1,11):
        product = number * number1
        string1 = string1 + str("{:5}".format(product))

print(string1)
        
        
    