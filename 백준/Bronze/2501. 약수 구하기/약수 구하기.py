n, k = map(int, input().split())
cnt = 0
ans = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
        ans = i
        if cnt == k:
            break
if cnt < k:
    print(0)
else:
    print(ans)
    