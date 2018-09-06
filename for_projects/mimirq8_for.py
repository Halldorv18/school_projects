stars = int(input("Max number of stars: ")) # Do not change this line

for x in range(1,stars+1):
    print("*"*x)
for x in range(stars-1,0, -1):
    print("*"*x)