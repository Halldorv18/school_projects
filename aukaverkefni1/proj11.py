a = int(input("Input an integer: "))
b = int(input("Input another interger: "))
choice = int(input("Input a choice: "))
if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
else: 
    print("Invalid input!")