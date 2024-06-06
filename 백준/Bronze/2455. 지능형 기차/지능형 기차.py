passanger = 0
M = 0
for _ in range(4):
    o, i = map(int, input().split())
    passanger -= o
    passanger += i
    if passanger > M:
        M = passanger
        
print(M)