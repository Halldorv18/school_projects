height_str = input("Insert height: ")
height_int = int(height_str)
length_str = input("Insert length: ")
length_int = int(length_str)
def area_of_rectangle(a, b):
    result = a * b
    return result
answer = area_of_rectangle(height_int, length_int)
print("The area of the rectangle is:", answer)
