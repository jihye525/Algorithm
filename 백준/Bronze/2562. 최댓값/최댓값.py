M = 0
n = 0
for i in range(9):
    a = int(input())
    if a > M:
        M = a
        n = i + 1
                 
print(M)
print(n)