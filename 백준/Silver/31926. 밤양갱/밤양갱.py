import sys, math
input = sys.stdin.readline
n = int(input())
sec = 8 + int(math.log2(n)) + 2
print(sec)