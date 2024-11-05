from collections import deque
tc = int(input())
dr = [1, 2, 2, 1, -1, -2, -2, -1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(cr, cc):
    global board
    queue = deque()
    queue.append([cr, cc])
    while queue:
        crr, ccc = queue.popleft()
        for i in range(8):
            move_r, move_c = crr + dr[i], ccc + dc[i]
            if 0 <= move_r < n and 0 <= move_c < n:
                if board[move_r][move_c] == -1:
                    board[move_r][move_c] = board[crr][ccc] + 1
                    queue.append([move_r, move_c])


for _ in range(tc):
    n = int(input())
    board = [[-1] * n for _ in range(n)]
    nr, nc = map(int, input().split())
    r, c = map(int, input().split())
    board[nr][nc] = 0
    bfs(nr, nc)
    print(board[r][c])
