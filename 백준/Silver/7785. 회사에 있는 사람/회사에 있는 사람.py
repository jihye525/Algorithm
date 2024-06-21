import sys
input = sys.stdin.readline
n = int(input())
lst = set()
for _ in range(n):
    a, b = input().split()
    if b == "enter":
        lst.add(a)
    else:
        lst.discard(a)


ans = sorted(list(lst), reverse=True)

for a in ans:
    print(a)