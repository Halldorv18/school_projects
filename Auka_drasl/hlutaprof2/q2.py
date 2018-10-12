def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
# The main program starts here
prime_list = []
user_input = input("Enter integers separated with commas: ")
integer_list = user_input.split(",")
try:
    integer_list = [int(x) for x in integer_list]
    sorted_list = sorted(integer_list)
    for integers in integer_list:
        if is_prime(integers) == True and integers not in prime_list:
            prime_list.append(integers)
    prime_list.sort()
    max_value = str(max(integer_list))
    min_value = str(min(integer_list))
    average = sum(integer_list)/len(integer_list)
    print("Input list: {}".format(integer_list))
    print("Sorted list:  {}".format(sorted_list))
    print("Prime list:  {}".format(prime_list))
    print("Min: {}, Max: {}, Average: {:.2f}".format(min_value, max_value, average))
except:
    print("Incorrect input!")








