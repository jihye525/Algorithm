import heapq
import sys
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    num = int(input())
    
    # 먼저 왼쪽에 넣기
    heapq.heappush(left_heap, -num)
    
    #숫자 맞추기 위해 오른쪽 힙으로 push
    heapq.heappush(right_heap, -heapq.heappop(left_heap))
    
    # 항상 왼쪽이 오른쪽보다 하나 크거나 같아야 함 
    if len(left_heap) < len(right_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    print(-left_heap[0])