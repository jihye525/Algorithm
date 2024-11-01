import sys
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())
A = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(n+1):
    A[i].sort()


def bfs():
    global r
    visited = [0] * (n + 1)
    queue = deque()
    queue.append(r)
    order = 1
    visited[r] = 1

    while queue:
        q = queue.popleft()
        for a in A[q]:
            if not visited[a]:
                order += 1
                visited[a] = order
                queue.append(a)

    print(*visited[1:], sep="\n")


bfs()