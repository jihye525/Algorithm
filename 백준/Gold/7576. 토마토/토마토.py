import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(m)]
tomatoes = deque()
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            tomatoes.append((i,j))


def one_day(tomatoes):
    temp = deque()
    while tomatoes:
        x, y = tomatoes.popleft()
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx <m and 0 <= ny < n and box[nx][ny] == 0:
                box[nx][ny] = 1
                temp.append((nx, ny))
    return temp


def solve():
    days = 0
    result = one_day(tomatoes)
    while len(result) > 0:
        days += 1
        result = one_day(result)

    if any(0 in row for row in box):
        print(-1)
    else:
        print(days)
solve()
