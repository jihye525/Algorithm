import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
A = [[] for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    A[a].append(b)
    A[b].append(a)


def bfs(v):
    global ans
    visited = [-1] * (n + 1)
    queue = deque()
    visited[v] = 0
    queue.append(v)

    while queue:
        candidate = queue.popleft()
        for friend in A[candidate]:
            if visited[friend] == -1:
                visited[friend] = visited[candidate] + 1
                queue.append(friend)

    return max(visited[1:])


result = []
for i in range(1, n + 1):
    result.append(bfs(i))

min_score = min(result)
candidates = [i for i in range(1, n + 1) if result[i-1] == min_score]

print(min_score, len(candidates))
print(*candidates)