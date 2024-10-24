import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N)]
visited = [False] * (N)
arrive = False

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False
    
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
    
for i in range(N): #시작점을 다르게 해서 DFS
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)