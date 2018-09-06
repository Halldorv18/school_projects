low = int(input("Please insert a low number"))
high = int(input("Please insert a high number"))

counter = low
while counter >= low and counter <= high :
    if counter % 2 != 0 :
        print(counter)
    counter += 1