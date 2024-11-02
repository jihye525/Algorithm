import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
ans = 0
while start <= end:
    mid = (start + end) // 2
    gain = sum([i - mid for i in trees if mid < i])
    if gain >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)