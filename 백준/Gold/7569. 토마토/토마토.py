import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
dr = [0, 0, 0, 1, 0, -1] #행
dc = [0, 0, 1, 0, -1, 0] #열
dh = [-1, 1, 0, 0, 0, 0] #높이


def bfs():
    queue = deque()
    all_even = 1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato_box[i][j][k] == 1 and not visited[i][j][k]:
                    visited[i][j][k] = 1
                    queue.append((i, j, k))
                if tomato_box[i][j][k] == 0:
                    all_even = 0

    if all_even:
        print(0)
        return

    while queue:
        i, j, k = queue.popleft()
        for a in range(6):
            dj = j + dr[a]
            dk = k + dc[a]
            di = i + dh[a]
            if (0 > dj or dj >= n) or (0 > dk or dk >= m) or (0 > di or di >= h):
                continue
            if tomato_box[di][dj][dk] == 0 and not visited[di][dj][dk]:
                visited[di][dj][dk] = 1
                queue.append((di, dj, dk))
                tomato_box[di][dj][dk] = tomato_box[i][j][k] + 1

    answer = 0
    for a in tomato_box:
        for b in a:
            for c in b:
                if c == 0:
                    print(-1)
                    exit(0)
            answer = max(answer, max(b))

    print(answer - 1)


bfs()