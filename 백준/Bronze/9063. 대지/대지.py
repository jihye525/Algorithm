def solve():
    n = int(input())
    lstx = []
    lsty =[]
    if n == 1:
        print(0)
        return 
    else:
        for _ in range(n):
            x, y = map(int, input().split())
            lstx.append(x)
            lsty.append(y)
        print((max(lstx)-min(lstx))*(max(lsty)-min(lsty)))
        
solve()