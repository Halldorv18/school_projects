lower = int(input("Input the lower number: "))
higher = int(input("Input the higher number: "))
if lower < higher:
    for number in range(lower, higher + 1):
        print(number)
else:
    print("Invalid input!")