int_1 = int(input("Input an integer: "))
int_2 = int(input("Input an integer: "))
int_3 = int(input("Input an integer: "))
if int_1 > int_2 and int_1 > int_3:
    print(int_1)
elif int_2 > int_1 and int_2 > int_3:
    print(int_2)
else:
    print(int_3)