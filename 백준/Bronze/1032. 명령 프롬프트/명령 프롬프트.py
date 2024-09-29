import sys
input = sys.stdin.readline
n = int(input())
mat = [input().strip() for _ in range(n)]
ans = ''
l = len(mat[0])
if n == 1:
    print(mat[0])
for i in range(l):
    c = mat[0][i]
    for j in range(1, n):
        if mat[j][i] != c:
            ans += '?'
            break
        if j == n-1:
            ans += c

print(ans)