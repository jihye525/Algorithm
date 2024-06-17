import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    istr = input().rstrip()
    t = (istr, len(istr))
    if t not in lst:
        lst.append(t)
lst.sort(key=lambda x: (x[1], x[0]))

for x, y in lst:
    print(x)