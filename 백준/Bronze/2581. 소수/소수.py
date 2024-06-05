m = int(input())
M = int(input())
ans = []
for i in range(m, M+1):
    isprime = 1
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            isprime = 0

    if isprime:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])