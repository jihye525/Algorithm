import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
mat = [list(input().rstrip()) for _ in range(n)]

def bfs(sr, sc, cnt):
    queue = deque()
    queue.append((sr, sc))
    colors[sr][sc] = cnt

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and colors[nr][nc] == 0:
                if mat[r][c] == mat[nr][nc]:
                    colors[nr][nc] = cnt
                    queue.append((nr, nc))

def not_red_green_bfs(sr, sc, cnt):
    queue = deque()
    queue.append((sr, sc))
    colors[sr][sc] = cnt

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and colors[nr][nc] == 0:
      
                if (mat[r][c] in 'RG' and mat[nr][nc] in 'RG') or mat[r][c] == mat[nr][nc]:
                    colors[nr][nc] = cnt
                    queue.append((nr, nc))

colors = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if colors[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)
red_green = cnt

colors = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if colors[i][j] == 0:
            cnt += 1
            not_red_green_bfs(i, j, cnt)
color_blind = cnt

print(red_green, color_blind)