import heapq
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    queue = []
    reversed_queue = []
    m = int(input())
    visited = [False] * m
    for i in range(m):
        oper, num = input().split()
        if oper == "I":
            heapq.heappush(queue, (-int(num), i))
            heapq.heappush(reversed_queue,(int(num), i))
        elif oper == "D" and num == '1' and queue:
            while queue and visited[queue[0][1]]:
                heapq.heappop(queue)
            if queue:
                visited[queue[0][1]] = True
                heapq.heappop(queue)
        elif oper == "D" and num == '-1' and reversed_queue:
            while reversed_queue and visited[reversed_queue[0][1]]:
                heapq.heappop(reversed_queue)
            if reversed_queue:
                visited[reversed_queue[0][1]] = True
                heapq.heappop(reversed_queue)

    while queue and visited[queue[0][1]]:
        heapq.heappop(queue)
    while reversed_queue and visited[reversed_queue[0][1]]:
        heapq.heappop(reversed_queue)

    if not queue or not reversed_queue:
        print("EMPTY")
    else:
        n1, idx1 = heapq.heappop(queue)
        n2, idx2 = heapq.heappop(reversed_queue)
        print(-n1, n2)