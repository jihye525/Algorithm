n, m = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1.sort()
lst2.sort()
cnt = 0
i = j = 0
while i < n and j < m:
    if lst1[i] == lst2[j]:
        cnt += 1
        i += 1
        j += 1
    elif lst1[i] > lst2[j]:
        j += 1
    elif lst1[i] < lst2[j]:
        i += 1

print(n + m - 2 * cnt)