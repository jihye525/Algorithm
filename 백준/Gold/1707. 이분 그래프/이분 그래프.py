
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, list):
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if visited[node]:
            continue

        visited[node] = True

        if not (set1 & set(list[node])):  # set1에 인접한 노드가 없는 경우
            set1.add(node)
        elif not (set2 & set(list[node])):  # set2에 인접한 노드가 없는 경우
            set2.add(node)
        else:  # 양 집합 모두 인접 노드가 존재하는 경우
            return False

        queue.extend(list[node])

    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    A = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    set1, set2 = set(), set()
    
    for _ in range(e):
        v1, v2 = map(int, input().split())
        A[v1].append(v2)
        A[v2].append(v1)
  
    result = True
    for start in range(1, v + 1):
        if visited[start]:
            continue

        result = result and bfs(start, A)

    if result:
        print('YES')
    else:
        print('NO')