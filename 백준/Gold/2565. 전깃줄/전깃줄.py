import sys
input = sys.stdin.readline

n = int(input())
power_line = [list(map(int, input().split())) for _ in range(n)]
power_line.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if power_line[j][1] < power_line[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
