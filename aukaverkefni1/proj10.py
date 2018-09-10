int_1 = int(input("Input and integer: "))
if 0 <= int_1 <= 10:
    print("Less than 10.")
elif 10 < int_1 < 20:
    print("Between 10 and 20.")
elif 20 <= int_1:
    print("the value is too high!")
else:
    print("too low!")
