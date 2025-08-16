import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def recur(r, c):
    global answer
    if r == n-1 and c == m -1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    route = 0
    for dr, dc in ((1, 0), (0, 1), (0, -1), (-1,0)):
        nr, nc = r + dr, c + dc
        if 0<= nr < n and 0<= nc < m:
            if mat[nr][nc] < mat[r][c]:
                route += recur(nr, nc)

    dp[r][c] = route
    return dp[r][c]

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

recur(0, 0)
print(dp[0][0])