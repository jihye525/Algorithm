tc = int(input())
for _ in range(tc):
    lst = input().split()
    ans = float(lst[0])
    for i in range(1, len(lst)):
        if lst[i] == "@":
            ans *= 3
        if lst[i] == "%":
            ans += 5
        if lst[i] == "#":
            ans -= 7
    print('%.2f'% ans)
