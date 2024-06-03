n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        s = ""
        for j in range(1, 2*n + 1):
            if j % 2 == 0:
                s += "*"
            else:
                s += " "
        print(s)
    else:
        s = ""
        for j in range(1, 2*n + 1):
            if j % 2 == 0:
                s += " "
            else:
                s += "*"
        print(s)