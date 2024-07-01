n = int(input())
t = 1
i = 1
cnt = 0
while t <= n:
    i += 2
    t += i
    cnt += 1


print(cnt)