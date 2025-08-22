import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int, input().split())
boxes = [list(list(map(int, input().split())) for _ in range(m)) for _ in range(h)]

tomatoes = deque()
for i in range(h):
    for j in range(m):
        for k in range(n):
            if boxes[i][j][k] == 1:
                tomatoes.append((i, j, k))


def bfs():
    global tomatoes, days
    temp = deque()
    while tomatoes:
        k, r, c = tomatoes.popleft()
        for dr, dc, dh in ((1,0,0), (0,1,0), (-1, 0, 0), (0, -1, 0), (0,0,1), (0, 0, -1)):
            nr, nc, nh = r + dr, c + dc, k + dh
            if 0<=nr<m and 0<=nc<n and 0 <= nh < h and boxes[nh][nr][nc] == 0:
                boxes[nh][nr][nc] = 1
                temp.append((nh, nr, nc))

    if len(temp) > 0:
        tomatoes = temp
        days += 1
        return True
    else:
        return False


days = 0
while True:
    if not bfs():
        break

for box in boxes:
    for row in box:
        for t in row:
            if t == 0:
                days = -1

print(days)
