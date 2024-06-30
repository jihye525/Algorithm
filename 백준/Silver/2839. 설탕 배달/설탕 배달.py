n = int(input())
lst = []
for x in range(0, 1001):
    for y in range(0, 1667):
        if x * 5 + y * 3 == n:
            lst.append((x, y))

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst[-1]))