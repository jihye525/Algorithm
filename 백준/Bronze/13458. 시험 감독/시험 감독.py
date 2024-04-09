from collections import deque
import sys
import math

read = sys.stdin.readline
n = int(read())
lst = list(map(int, read().split()))
b, c = map(int, read().split())
ans = 0

for i in range(n):
    if lst[i] - b <= 0:
        ans += 1
    else:
        ans += 1 + math.ceil((lst[i] - b) / c)

print(ans)