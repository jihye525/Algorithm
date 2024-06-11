l = [list(map(int, input().split())) for _ in range(9)]
M = 0
Mr, Mc = 0, 0
for i in range(9):
    for j in range(9):
        if l[i][j] > M:
            M = l[i][j]
            Mr, Mc = i, j

print(M)
print(Mr+1, Mc+1)