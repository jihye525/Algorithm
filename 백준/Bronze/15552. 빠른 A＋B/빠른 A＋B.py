import sys

read = sys.stdin.readline
n = int(read())

for _ in range(n):
    a, b = map(int, read().split())
    print(a+b)