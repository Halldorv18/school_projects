high = int(input("Please input the higher number"))
low = int(input("Please input the lower number"))
counter = low
while counter >= low and counter <= high:
    if counter %2 != 0:
        print(counter)
    counter += 1
