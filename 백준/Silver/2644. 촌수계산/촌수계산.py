
import sys
input = sys.stdin.readline
n = int(input())
h1, h2 = map(int, input().split())
m = int(input())
family = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)


def dfs(v, chon):
    if h2 == v:
        print(chon)
        return

    for r in family[v]:
        if not visited[r]:
            visited[r] = True
            dfs(r, chon + 1)


visited = [False] * (n + 1)
visited[h1] = True
dfs(h1, 0)
if not visited[h2]:
    print(-1)