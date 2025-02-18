import sys
input= sys.stdin.readline
N = int(input())
M = int(input())
distance = [[sys.maxsize for _ in range(N + 1)] for i in range(N + 1)]

#시작 도시와 도착 도시가 같은 경우는 없다 -> 0
for i in range(1, N + 1):
    distance[i][i] = 0

#같은 노선이면 가장 적은 비용만 저장
for i in range(M):
    s, e, v = map(int, input().split())
    if distance[s][e] > v:
        distance[s][e] = v

#플로이드-워셜 수행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
        
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()