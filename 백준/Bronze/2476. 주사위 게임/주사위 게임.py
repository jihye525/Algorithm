t = int(input())
lst = []
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b == c:
        lst.append(10000 + a * 1000)

    elif a == b or a == c:
        lst.append(1000 + 100 * a)

    elif b == c:
        lst.append(1000 + 100 * b)

    else:
        lst.append(100 * max(a, b, c))

print(max(lst))