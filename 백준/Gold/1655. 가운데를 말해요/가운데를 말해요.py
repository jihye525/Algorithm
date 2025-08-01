import heapq
import sys
input = sys.stdin.readline

n = int(input())
left_heap = []  
right_heap = []  

for _ in range(n):
    num = int(input())

    heapq.heappush(left_heap, -num)

    heapq.heappush(right_heap, -heapq.heappop(left_heap))

    if len(left_heap) < len(right_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    print(-left_heap[0])