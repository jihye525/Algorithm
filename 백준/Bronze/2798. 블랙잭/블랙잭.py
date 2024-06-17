import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i]+lst[j]+lst[k] <= m:
                ans.append(lst[i]+lst[j]+lst[k])

print(max(ans))