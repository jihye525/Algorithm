t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    
    for _ in range(n):
        a, p = map(int, input().split())
        s += a * p
        
    print(s)