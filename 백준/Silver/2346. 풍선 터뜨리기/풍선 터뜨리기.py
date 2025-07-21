from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
moves = list(map(int, input().split()))

balloons = deque((i + 1, move) for i, move in enumerate(moves))

result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(idx)

    if not balloons:
        break

    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-(move))


print(' '.join(map(str, result)))