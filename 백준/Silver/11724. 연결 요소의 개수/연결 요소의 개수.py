import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
connect = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)


def bfs():
    global n
    idx = 1
    for i in range(n+1):
        if not visited[i]:
            idx = i
    queue = deque()
    queue.append(idx)
    visited[idx] = 1

    while queue:
        node = queue.popleft()
        for next_node in connect[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)


visited = [0] * (n+1)
answer = 0
while True:
    if sum(visited) == n:
        break
    bfs()
    answer += 1
print(answer)