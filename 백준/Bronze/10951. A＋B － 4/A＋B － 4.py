import sys
si = sys.stdin.read().splitlines()

for l in si:
    a, b = map(int, l.split())
    print(a+b)