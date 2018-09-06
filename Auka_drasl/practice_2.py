# Æfing 1
number = input("Pick a number ")
number_int = int(number)
if number_int == 42:
    print("The answer to the Ultimate question of life, the Universe and Everything is ", number_int)
else:
    print("The answer to the Ultimate question of life, the Universe and Everything is not ", number_int)

#Æfing 2
a = input("Pick a number ->")
b = input ("Pick a second number ->")
a_int = int(a)
b_int = int(b)
if a_int > b_int:
    print(a_int)
elif a_int < b_int:
    print(b_int)

#Æfing 3
age = int(input("What is your age? "))
if age > 0:
    print("You are ", age, " years old.")
else:
    print("Invalid input")

#Æfing 4
number_int = int(input("Pick a number "))
if number_int < 0:
    print(number_int * (-1))
else:
    print(number_int)

#Æfing 5
a_int = int(input("Pick a number "))
b_int = int(input("Pick another number "))
if a_int < 0 or b_int < 0:
    print("Invalid input")
else:
    print(a_int + b_int)

#Æfing 6
a = input("Input the first number ")
b = input("Input the second number")
c = input("Input the answer ")
a_int = int(a)
b_int = int(b)
c_int = int(c)
if a_int * b_int == c_int:
    print("Good job!")
else:
    print("Not quite right, go practice more!")

#Æfing 7
name = input("Insert your name here ")
weight = input("Insert your weight in kilograms ")
weight_int = int(weight)
if weight_int > 90:
    print(a, " competes in heavyweight.")
elif weight_int <= 90 and weight_int >= 60:
    print(name, " competes in middleweight")
elif weight_int < 60:
    print(name, " competes in lightweight")
else:
    print("Invalid input")

#Æfing 8
number1 = input("Please insert a number ")
number2 = input("Please insert another number ")
number3 = input("Please insert another number ")
number1_int = int(number1)
number2_int = int(number2)
number3_int = int(number3)
if number1_int >= number2_int and number1_int >= number3_int:
    print(number1_int)
elif number2_int >= number1_int and number2_int >= number3_int:
    print(number2_int)
elif number3_int >= number1_int and number3_int >=number2_int:
    print(number3_int)

#Æfing 9
number1 = input("Please enter a number ")
number2 = input("Please enter a number ")
number3 = input("Please enter a number ")
number1_int = int(number1)
number2_int = int(number2)
number3_int = int(number3)