num = 10

counter = 1

while num < 100: 
    if num == num ** 2 % 100:
        print(num)
        break
    num += 1