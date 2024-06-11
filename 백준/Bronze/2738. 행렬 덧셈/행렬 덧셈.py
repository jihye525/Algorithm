n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l2 = [list(map(int, input().split())) for _ in range(n)]

s = [[l[j][i]+l2[j][i] for i in range(m)] for j in range(n)]

for i in range(n):
    print(" ". join(map(str, s[i])))