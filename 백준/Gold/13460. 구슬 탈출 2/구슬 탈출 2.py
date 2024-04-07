from collections import deque
import sys

read = sys.stdin.readline
N, M = map(int, read().split())
graph = []
for i in  range(N):
    graph.append(list(read()))
    for j in range(M):
        if graph[i][j] == 'R': # 빨간구슬 위치
            rx, ry = i, j
        elif graph[i][j] == 'B': # 파란구슬 위치
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by)])
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0

    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if count > 10:
                print(-1)
                return
            if graph[rx][ry] == 'O':
                print(count)
                return 

            for d in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by
                dr, db = 0, 0
                while True:
                    nrx, nry = nrx + dx[d], nry + dy[d]
                    dr += 1
                    if graph[nrx][nry] == '#':
                        nrx -= dx[d]
                        nry -= dy[d]
                        dr -= 1
                        break
    
                    if graph[nrx][nry] == 'O':
                        break
    
                while True:
                    nbx, nby = nbx + dx[d], nby + dy[d]
                    db += 1
                    if graph[nbx][nby] == '#':
                        nbx -= dx[d]
                        nby -= dy[d]
                        db -= 1
                        break
    
                    if graph[nbx][nby] == 'O':
                        break
    
                if graph[nbx][nby] == 'O':  # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                    continue
    
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if dr < db: # 더 많이 이동한 구슬을 한 칸 뒤로 이동
                        nbx -= dx[d]
                        nby -= dy[d]
                    else:
                        nrx -= dx[d]
                        nry -= dy[d]
    
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))

        count += 1
    print(-1)

bfs(rx, ry, bx, by)