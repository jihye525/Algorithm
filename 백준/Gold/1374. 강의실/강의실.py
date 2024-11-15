import sys
import heapq
input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: x[1])
classroom = []
max_classroom = 0
for lec in schedule:
    while classroom and classroom[0] <= lec[1]:
        heapq.heappop(classroom)
    heapq.heappush(classroom, lec[-1])
    max_classroom = max(max_classroom, len(classroom))

print(max_classroom)