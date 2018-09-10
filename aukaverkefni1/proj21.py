turns = int(input("Input turns: "))
while turns != 0:
    x = int(input("Input and integer"))
    if x % 2 != 0:
        print(x)
    turns -= 1