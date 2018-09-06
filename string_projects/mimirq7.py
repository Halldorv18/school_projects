

my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
bstr = ""
quote = my_int
if my_int == 0:
    bstr = "0"
else:
    while quote != 0:
        if quote % 2 == 0:
            bstr += "0"
            quote //= 2
        else:
            bstr += "1"
            quote //= 2

print("The binary of", my_int, "is", bstr[::-1])
