low = int(input("Please enter a low number"))
high = int(input("Please enter a high number"))
counter = low
sum = 0
while counter <= high and counter >= low:
    if counter % 2 == 0:
        sum += counter
    counter += 1
print (sum)