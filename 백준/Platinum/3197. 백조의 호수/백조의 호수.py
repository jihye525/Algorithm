import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
lake = [list(input().strip()) for _ in range(R)]
swans = []
water_q = deque()
visited_water = [[0]*C for _ in range(R)]

# 초기 물, 백조 위치 저장
for i in range(R):
    for j in range(C):
        if lake[i][j] != 'X':
            water_q.append((i, j))
            visited_water[i][j] = 1
        if lake[i][j] == 'L':
            swans.append((i, j))

swan_q = deque()
visited_swan = [[0]*C for _ in range(R)]
swan_q.append(swans[0])
visited_swan[swans[0][0]][swans[0][1]] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move_swan():
    next_swan_q = deque()
    while swan_q:
        x, y = swan_q.popleft()
        if (x, y) == swans[1]:
            return True
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and not visited_swan[nx][ny]:
                visited_swan[nx][ny] = 1
                if lake[nx][ny] == 'X':
                    next_swan_q.append((nx, ny))
                else:
                    swan_q.append((nx, ny))
    return next_swan_q

def melt():
    next_water_q = deque()
    while water_q:
        x, y = water_q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and not visited_water[nx][ny]:
                visited_water[nx][ny] = 1
                if lake[nx][ny] == 'X':
                    lake[nx][ny] = '.'
                    next_water_q.append((nx, ny))
                else:
                    water_q.append((nx, ny))
    return next_water_q

days = 0
while True:
    swan_q = move_swan()
    if swan_q is True:
        print(days)
        break
    water_q = melt()
    days += 1