import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]


def recur(i, j):
    if dp[i][j] != 0:
        return dp[i][j]

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < n:
            if forest[nx][ny] > forest[i][j]:
                dp[i][j] = max(dp[i][j], recur(nx, ny) + 1)

    return dp[i][j]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        recur(i, j)
print(max(map(max,dp))+1)

