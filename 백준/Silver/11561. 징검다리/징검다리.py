import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    start = 1
    end = n
    bridge = 0

    while start <= end:
        mid = (start + end) // 2
        if (mid * (mid + 1)) // 2 <= n:
            start = mid + 1
            bridge = mid
        else:
            end = mid - 1

    print(bridge)