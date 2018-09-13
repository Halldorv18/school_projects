low = int(input("Please pick a random number "))
high = int(input("Please pick another random number "))
sum = 0

counter = low
while counter >= low and counter <= high:
    sum += counter
    counter += 1
print(sum)
