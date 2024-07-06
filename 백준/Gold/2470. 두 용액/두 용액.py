n = int(input())
lst = list(map(int, input().split()))
lst.sort()
i = 0
j = n - 1
ans = [0, n - 1]
v = abs(lst[i] + lst[j])
while i < j:
    if abs(lst[i] + lst[j]) == 0:
        ans = [i, j]
        break
    elif abs(lst[i] + lst[j]) < v:
        ans = [i, j]
        v = abs(lst[i] + lst[j])

    if lst[i] + lst[j] < 0:
        i += 1
    else:
        j -= 1

print(lst[ans[0]], lst[ans[1]])