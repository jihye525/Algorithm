def fac(n, s):
    if n <= 1:
        print(s)
        return

    return fac(n - 1, s * n)


N = int(input())

fac(N, 1)