size_str = input("Insert the size of the list: ")
size_int = int(size_str)
size_int_perm = size_int
number_list= []
maxVal = number_list[int(0)]
while size_int > 0:
    number_str = input("Please enter a number")
    number_int = int(number_str)
    number_list.append(number_int)
    size_int -= 1
for i in range(0, size_int_perm, 1): #Virkar ekki
    if maxVal > number_list[i]:
        maxVal = number_list[i]
print(maxVal)

# Læra max á frumstæðari máta!

