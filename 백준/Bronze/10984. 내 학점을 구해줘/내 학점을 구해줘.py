t = int(input())
for _ in range(t):
    n = int(input())
    s = 0.0
    gs = 0
    for _ in range(n):
        g, c = map(float, input().split())
        gs += g
        s += g * c
    print("%d %.1f"%(gs,s/gs))