import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    s = input().rstrip()
    a, b = s.split(".")
    if b in d:
        d[b] = d[b] + 1
    else:
        d[b] = 1

lst = []
for k, v in d.items():
    lst.append([k, v])
lst.sort()
for k, v in lst:
    print(k, v)