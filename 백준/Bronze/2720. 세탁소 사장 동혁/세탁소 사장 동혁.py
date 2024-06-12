t = int(input())
for _ in range(t):
    exg = int(input())
    print(exg // 25, end=' ')
    exg %= 25
    print(exg // 10, end=' ')
    exg %= 10
    print(exg // 5, end=' ')
    print(exg % 5)