import sys
input = sys.stdin.readline
n = int(input())
poles = [list(map(int, input().split())) for _ in range(n)]
poles.sort()
dp = [1]*n

for i in range(n):
    for j in range(0, i):
        if poles[j][1] < poles[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

