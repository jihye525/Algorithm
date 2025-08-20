import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
computers = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        node = queue.popleft()
        for c in computers[node]:
            if not visited[c]:
                visited[c] = 1
                queue.append(c)


visited = [0] * (n+1)
bfs()
print(sum(visited)-1)