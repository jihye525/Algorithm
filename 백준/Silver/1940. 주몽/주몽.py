n = int(input())
m = int(input())
lst = list(map(int,input().split()))
lst.sort()
i = 0
j = n-1
cnt = 0
while i < j:
    if lst[i] + lst[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif lst[i] + lst[j] < m:
        i += 1
    else:
        j -= 1
print(cnt)