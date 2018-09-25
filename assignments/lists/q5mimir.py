def input_vector(size):
    vector = []
    for index in range(1,size+1):
        element = float(input("Element no {}: ".format(index)))
        vector.append(element)
    return vector
def dot_product(vector1, vector2):
    summa = 0
    for index in range(0,len(vector1)):
        summa += vector1[index] * vector2[index] 
    return summa

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))