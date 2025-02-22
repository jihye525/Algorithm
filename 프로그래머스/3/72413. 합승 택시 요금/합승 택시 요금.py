import sys
def solution(n, s, a, b, fares):
    road = [[sys.maxsize] * (n + 1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        road[i][i] = 0
        
    for c, d, f in fares:
        road[c][d] = f
        road[d][c] = f
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if road[i][j] > road[i][k] + road[k][j]:
                    road[i][j] = road[i][k] + road[k][j]
    
    min_fares = road[s][a] + road[s][b]
    
    for k in range(1, n + 1):
        if min_fares > road[s][k] + road[k][a] + road[k][b]:
            min_fares = road[s][k] + road[k][a] + road[k][b]
    
        
    return min_fares