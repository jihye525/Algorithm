import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda x: (x[0], x[1]))

for x, y in lst:
    print(x, y)