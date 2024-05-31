t = int(input())

for _ in range(t):
    n = int(input())
    max_c = 0
    max_p = ""
    for _ in range(n):
        c, p = input().split()

        if int(c) > max_c:
            max_c = int(c)
            max_p = p

    print(max_p)