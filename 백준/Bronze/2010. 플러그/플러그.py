import sys

si = list(map(int, sys.stdin.read().splitlines()))

print(sum(si)-2*si[0]+1)