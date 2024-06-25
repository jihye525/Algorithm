import sys, math
m, n = map(int, sys.stdin.readline().split())
for i in range(m, n+1):
    is_prime = 1
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    for j in range(2, int(math.sqrt(i)) + 2):
        if i % j == 0:
            is_prime = 0
            break
    if is_prime:
        print(i)