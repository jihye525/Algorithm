import sys
input = sys.stdin.readline
x, y = map(int, input().split())
z = int((y * 100) / x)

if z > 98:
    print(-1)
else:
    start = 0
    end = 1000000000

    while start <= end:
        mid = (start + end) // 2
        if int(((y + mid)  * 100)/ (x + mid)) > z:
            end = mid - 1
        else:
            start = mid + 1

    print(start)
    