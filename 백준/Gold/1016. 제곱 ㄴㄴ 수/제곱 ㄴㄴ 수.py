m, M = map(int, input().split())
lst = [True] * (M - m + 1)
ans = M - m + 1

for i in range(2, int(M ** 0.5) + 1):
    square = i ** 2
    for j in range((((m-1)//square)+1)*square, M+1, square):
        if lst[j-m]:
            lst[j-m] = False
            ans -= 1

print(ans)