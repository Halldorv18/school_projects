intial_value = int(input("Initial value: "))
steps = int(input("Step: "))
values = ""
sum_of_numbers = 0

for number in range(intial_value, 100 , steps):
        if sum_of_numbers < 100:
            sum_of_numbers += number
            values += (str(number) + " ")

print(values)
print("Sum of series:", sum_of_numbers)

