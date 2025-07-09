from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0]  = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


bfs()
print(visited[n - 1][m - 1])