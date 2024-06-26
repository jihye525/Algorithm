def fiv(n, a, b):
    if n == 0:
        print(a)
        return 
    return fiv(n-1, b, a+b)

n = int(input())
fiv(n, 0, 1)
    