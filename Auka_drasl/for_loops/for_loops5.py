countdown_str = input("Insert time: ")
countdown_int = int(countdown_str)
for number in range(countdown_int, 0, -1):
    print(number)
print("Boom!")