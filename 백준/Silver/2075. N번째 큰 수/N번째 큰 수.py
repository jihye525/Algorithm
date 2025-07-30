import heapq
import sys
input = sys.stdin.readline

n = int(input())

hq = []
now = 0
for _ in range(n):
    mat = list(map(int, input().split()))
    for j in range(n):
        if len(hq) < n:
            heapq.heappush(hq, mat[j])
        else:
            if hq[0] < mat[j]:
                heapq.heappushpop(hq, mat[j])

print(heapq.heappop(hq))