import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort()
    count = 1
    min_i = scores[0][1]
    for i in range(1, n):
        if scores[i][1] < min_i:
            count += 1
            min_i = min(min_i, scores[i][1])

    print(count)