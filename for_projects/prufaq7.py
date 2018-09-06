top_num = int(input("Input a number between 0 and 999: "))
str_top_num = str(top_num)
length = len(str_top_num)
first_number = top_num // 100
second_numer = (top_num // 10) % 10
third_number = top_num % 100
first_number1 = top_num // 10
second_number1 = top_num % 10 
for number in range(1, top_num):
    for number in range(100,1000):
        if number == ((number//100)**length) + (((number // 10) % 10)**length) + ((number%100)**length):
            print(number)
    for number in range(10, 100):
        if number == (number//10)**length + (number%10)**length:
            print(number)
    for number in range(0, 10):
        if number == (number**length):
            print(number)