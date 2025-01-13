import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = list(tuple(map(int, input().split())) for _ in range(M))
INF = 5000000
distance = [0, 0] + [INF] * (N-1)

for i in range(N-1):
    for j in range(M):
        s, e, t = edges[j]
        if distance[s] != INF and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

negative_cycle = False # 무한 음수 사이클 여부 체크

for i in range(M):
    s, e, t = edges[i]
    if distance[s] != INF and distance[e] > distance[s] + t:
        negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for d in distance[2:]:
        if d == INF:
            print(-1)
        else:
            print(d)