
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list


def even_sum(a_list):
    list_of_ints = [int(i) for i in a_list]
    sum_of_even = [i for i in list_of_ints if i % 2 == 0]
    result = sum(sum_of_even)
    return result
# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
