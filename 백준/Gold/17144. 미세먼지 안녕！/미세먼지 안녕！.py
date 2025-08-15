import sys
from collections import deque
input = sys.stdin.readline

# 입력
r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치
air_cleaner = []
for i in range(r):
    if room[i][0] == -1:
        air_cleaner.append(i)

# 확산
def diffuse():
    spread = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                amount = room[i][j] // 5
                cnt = 0
                for dx, dy in ((0,1),(1,0),(-1,0),(0,-1)):
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        spread[nx][ny] += amount
                        cnt += 1
                room[i][j] -= amount * cnt
    # 확산된 양 더하기
    for i in range(r):
        for j in range(c):
            room[i][j] += spread[i][j]

# 공기청정기 작동
def clean():
    top = air_cleaner[0]
    bottom = air_cleaner[1]

    # 위쪽 반시계
    for i in range(top-1, 0, -1):
        room[i][0] = room[i-1][0]
    for j in range(c-1):
        room[0][j] = room[0][j+1]
    for i in range(top):
        room[i][c-1] = room[i+1][c-1]
    for j in range(c-1, 1, -1):
        room[top][j] = room[top][j-1]
    room[top][1] = 0

    # 아래쪽 시계
    for i in range(bottom+1, r-1):
        room[i][0] = room[i+1][0]
    for j in range(c-1):
        room[r-1][j] = room[r-1][j+1]
    for i in range(r-1, bottom, -1):
        room[i][c-1] = room[i-1][c-1]
    for j in range(c-1, 1, -1):
        room[bottom][j] = room[bottom][j-1]
    room[bottom][1] = 0

for _ in range(t):
    diffuse()
    clean()

total = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            total += room[i][j]

print(total)