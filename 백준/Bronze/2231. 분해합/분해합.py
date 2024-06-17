import sys

def solve():
    input = sys.stdin.readline
    ans = 0
    n = int(input())
    if n <= 10:
        if n % 2 == 0:
            print(n // 2)
            return
        else:
            print(0)
            return

    for i in range(10, n+1):
        s = str(i)
        hap = i
        for num in s:
            hap += int(num)

        if hap == n:
            ans = i
            break

    print(ans)


solve()