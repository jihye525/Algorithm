tc = int(input())
for _ in range(tc):
    n, alpha = input().split()
    ans = ""
    for a in alpha:
        ans += a*int(n)
    print(ans)