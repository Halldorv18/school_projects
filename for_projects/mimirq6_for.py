top_num = int(input("Upper number for the range: ")) # Do not change this line



for cb in range(5,top_num+1):
    sum_of_divisors=0
    for deilir in range(1, cb):
        if cb % deilir == 0:
            sum_of_divisors +=deilir
      
    if cb == sum_of_divisors:
        print(cb)