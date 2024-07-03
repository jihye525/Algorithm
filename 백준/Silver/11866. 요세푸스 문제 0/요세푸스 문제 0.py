from collections import deque

n, k = map(int,input().split())
d = deque([i for i in range(1, n + 1)])
ans = ""
while True:
    if len(d) == 0:
        break

    for _ in range(k-1):
        d.append(d.popleft())
    ans += str(d.popleft()) +", "

print("<"+ans[:-2]+">")