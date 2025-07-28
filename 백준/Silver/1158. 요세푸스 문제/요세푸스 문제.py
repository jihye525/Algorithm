from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dq = deque(list(i for i in range(1, n + 1)))
ans = []
for _ in range(n):
    dq.rotate(-k)
    ans.append(dq.pop())

print("<"+", ".join(map(str,ans))+">")