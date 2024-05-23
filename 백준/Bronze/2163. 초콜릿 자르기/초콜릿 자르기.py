n, m = map(int, input().split())
cnt = 0
for i in range(n):
    cnt += 1
    for j in range(m-1):
        cnt += 1

print(cnt - 1)
