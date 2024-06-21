import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().rstrip().split()))
s = dict().fromkeys(lst, 0)

for i in lst:
    s[i] += 1

m = int(input())
qlst = list(map(int, input().rstrip().split()))
for q in qlst:
    if s.get(q):
        print(s[q], end=" ")
    else:
        print(0, end=" ")