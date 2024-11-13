import sys
input = sys.stdin.readline
n = int(input())
scores = [int(input()) for _ in range(n)]
now = scores[-1]
down = 0
for i in range(n-2, -1, -1):
    if scores[i] >= now:
        down += scores[i] - now + 1
        scores[i] -= scores[i] - now + 1
    now = scores[i]

print(down)