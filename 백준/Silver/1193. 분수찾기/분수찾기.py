n = int(input())
i = 1
while n > i:
    n -= i
    i += 1

if  i % 2 == 0:
    a, b = 1, i
    for _ in range(n-1):
        a += 1
        b -= 1
    print(str(a) + "/" + str(b))
else:
    a, b = i, 1
    for _ in range(n-1):
        a -= 1
        b += 1
    print(str(a) + "/" + str(b))