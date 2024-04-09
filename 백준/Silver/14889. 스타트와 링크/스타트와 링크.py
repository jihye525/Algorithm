import sys

read = sys.stdin.readline
n = int(read())
s = [list(map(int, read().split())) for _ in range(n)]
alst = []
blst = []
ans = []

def calc(alst, blst):
    global s
    global ans
    asum = bsum = 0
    for i in alst:
        for j in alst:
            asum += s[i][j]

    for i in blst:
        for j in blst:
            bsum += s[i][j]

    ans.append(abs(asum - bsum))

def dfs(alst, blst, n):
    if n == 0:
        if len(alst) == len(blst):
            calc(alst, blst)

    else:
        dfs(alst+[n-1], blst, n-1)
        dfs(alst, blst+[n-1], n-1)


dfs(alst, blst, n)
print(min(ans))
