n, x = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
for i in range(n):
    if lst[i] < x:
        ans.append(lst[i])

print(" ". join(str(x) for x in ans))