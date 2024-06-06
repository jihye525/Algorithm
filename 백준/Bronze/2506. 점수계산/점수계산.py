n = int(input())
lst = list(map(int, input().split()))
ds = 0
score = 0
if lst[0] == 1:
    ds += 1
    score += 1
for i in range(1, n):
    if lst [i] == 1:
        ds += 1
        score += ds
    else:
        ds = 0
print(score)