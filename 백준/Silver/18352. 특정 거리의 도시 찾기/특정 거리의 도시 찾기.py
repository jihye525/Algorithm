import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
bridge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    bridge[a].append(b)


def bfs(start):
    distance = [-1] * (N + 1)
    K_city = False
    queue = deque()
    queue.append(start)
    distance[start] = 0
    while queue:
        s = queue.popleft()
        for i in bridge[s]:
            if distance[i] == -1:
                distance[i] = distance[s] + 1
                queue.append(i)
                if distance[i] == K:
                    K_city = True

    for i in range(N + 1):
        if distance[i] == K:
            print(i)
            K_city = True
    if not K_city:
        print((-1))


bfs(X)