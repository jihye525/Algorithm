t = int(input())
lst = list(map(int, input().split()))
ans = 0
for n in lst:
    if n == 1:
        continue
    isprime = 1
    for i in range(2, n):
        if n % i == 0:
            isprime = 0
            break
    if isprime:
        ans += 1

print(ans)