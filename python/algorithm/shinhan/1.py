def fibo_recur(n):
    result = []
    if n <= 2:
        number = 1
    else:
       number = fibo_recur(n-1) + fibo_recur(n-2)
    return number

print(fibo_recur(6))