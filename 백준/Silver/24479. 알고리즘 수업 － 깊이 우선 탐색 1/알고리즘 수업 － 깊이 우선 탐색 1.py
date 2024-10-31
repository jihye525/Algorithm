import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline
n, m, r = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
idx = 1

def dfs(v):
    global idx
    visited[v] = idx
    for node in A[v]:
        if not visited[node]:
            idx += 1
            visited[node] = idx
            dfs(node)


for _ in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)


for i in range(n + 1):
    A[i].sort()


dfs(r)
for i in visited[1:]:
    print(i)