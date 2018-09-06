top_num = int(input("Input a number between 0 and 999: "))

for number in range(0, top_num):
   
    if 0 <= number < 10:
            print(number)
    
    if 10 <= number < 100:
        if number == ((number//10)**2) + ((number%10)**2):
            print(number)
   
    if 100 <= number < 1000:
        if number == ((number//100)**3) + (((number % 100) // 10)**3) + ((number%10)**3):
            print(number)
   
   
    