t = int(input())

for _ in range(t):
    n = int(input())
    max_uni = ""
    max_scr = 0
    for _ in range(n):
        uni, scr = input().split()
        if int(scr) > max_scr:
            max_uni = uni
            max_scr = int(scr)

    print(max_uni)

