n, m = map(int, input().split())
temp = []
for _ in range(n):
    temp.append(input())

dic = dict().fromkeys(temp, 1)
cnt = 0
for _ in range(m):
    if dic.get(input()):
        cnt += 1
print(cnt)