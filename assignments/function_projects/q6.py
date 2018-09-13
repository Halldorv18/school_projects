def fibo(n):
    if n == 1:
        print("1")
        return
    elif n == 2:
        print("1 1")
        return
    else:
        print("1 1", end='')
    value1 = 1
    value2 = 1
    for n in range(n-2):
        print("",value1+value2, end='')
        value1, value2 = value2, value1 + value2
n = int(input("Input the length of Fibonacci sequence (n>=1): "))
n_int = int(n)
fibo(n)