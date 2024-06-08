n = int(input())
lst = list(map(int, input().split()))
m = lst[0]
M = lst[0]
for a in lst:
    if a < m:
        m = a
    if M < a:
        M = a

print(m, M)