import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
mat = [[0] * n for _ in range(n)]
dr = [0, 1, 0, -1] #행 우하좌상
dc = [1, 0, -1, 0] #열
direction = 0
snake = deque([[0, 0]])
mat[0][0] = 1
play_time = 0
apples = int(input())

for _ in range(apples):
    r, c = map(int, input().split())
    mat[r-1][c-1] = 100

direction_n = int(input())
info = {}
for _ in range(direction_n):
    sec, direct = input().split()
    info[int(sec)] = direct

while True:
    nr, nc = snake.pop()
    mr, mc = nr+dr[direction], nc+dc[direction]
    snake.append([nr, nc])

    if mr < 0 or mr >= n or mc < 0 or mc >= n or [mr, mc] in snake: #벽에 막히거나 자신의 몸과 만나면 게임오버
        break

    if mat[mr][mc] != 100:  # 그냥 일반 칸이면
        r, c = snake.popleft() # 꼬리 한칸 줄이기
        mat[r][c] = 0
    mat[mr][mc] = 1 #머리 한칸 전진
    snake.append([mr, mc])

    play_time += 1 #게임 시간 +1
    if play_time in info.keys():
        if info[play_time] == "D": #오른쪽(시계 회전)
            direction = (direction + 1) % 4
        elif info[play_time] == "L": #왼쪽(반시계 회전)
            direction = (direction + 3) % 4

        # play = play[1:] #뱡향 지시 소멸

print(play_time+1)

