import sys
input = sys.stdin.readline
n = int(input())
square = 0
m = 1000
M = top = 0
arr = [0 for _ in range(1001)]
for _ in range(n):
    i, h = map(int, input().split())
    arr[i] = h
    M = max(i, M)
    m = min(i, m)
    top = max(h, top)

top_idx = arr.index(top)
now = 0
for i in range(m, top_idx+1):
    now = max(now, arr[i])
    square += now

now = 0
for i in range(M, top_idx, -1):
    now = max(now, arr[i])
    square += now

print(square)
