paper = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] += 1

s = 0
for i in range(100):
    s += paper[i].count(0)

print(10000 - s)