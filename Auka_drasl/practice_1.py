# Æfing 1

input_value = input("What is the answer to life? ")
my_str = "The answer to life, the universe and everything is"

print("The answer to life, the universe and everything is", input_value)

# Æfing 2
input_value1 = input("What's your age? ")
input_value2 = input("What's you favorite number? ")
print(int(input_value1) - int(input_value2))

# Æfing 3
input_value1 = input("Veldu tölu ")
input_value2 = input("Veldu aðra tölu ")
print(int(input_value1) + int(input_value2))

# Æfing 4
input_value1 = input('Veldu "X", X = ')
input_value2 = input('Veldu "Y", Y = ')
my_str = '"X" margfaldað með "Y" er jafnt og '
print(my_str, int(input_value1) * int(input_value2))

#Æfing 5
input_value1 = input("Insert your weight in kilograms ")
input_value2 = input("Insert your height in meters ")
my_str = "Your BMI is"
print(my_str, int(input_value1) / int(input_value2) ** 2)

# Æfing 6
number1 = input("Veldu heiltölu ")
number2 = input("Veldur aðra heiltölu ")
number3 = int(number1) // int(number2)
number4 = int(number1) % int(number2)
print("Quotient: ", number3, ", remainder: ", number4)

# Æfing 7
price = input("Please insert price here -> ")
tax = 0.255
print("The final price (with tax) is ", int(price) * (1 + tax))
