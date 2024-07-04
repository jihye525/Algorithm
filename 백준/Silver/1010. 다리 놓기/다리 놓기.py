tc = int(input())
for _ in range(tc):
    k, n = map(int, input().split())
    ans = 1
    for i in range(k+1, n+1):
        ans *= i
    for i in range(1, n - k + 1):
        ans //= i
    print(ans)  