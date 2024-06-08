import sys
lst = list(map(int, sys.stdin.read().splitlines()))
for i in range(1, 31):
    if i not in lst:
        print(i)
