n = int(input())
x = []
y = []
result = [-1]*n


for _ in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

for i in x:
    for j in y:
        dist = []
        for k in range(n):
            dist.append(abs(x[k]-i)+abs(y[k]-j))
        
        dist.sort()

        tmp = 0
        for m in range( len(dist)):
            d = dist[m]
            tmp += d
            if result[m] == -1:
                result[m] = tmp
            else:
                result[m] = min(tmp, result[m])

print(*result)