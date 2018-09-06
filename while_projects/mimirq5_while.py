n = int(input("Input a natural number: ")) # Do not change this line
counter = 2
prime = True
while counter < n:
    if n % counter == 0:
        prime = False
    counter += 1 
if prime:
    print("Prime")
else:
    print("!Prime")