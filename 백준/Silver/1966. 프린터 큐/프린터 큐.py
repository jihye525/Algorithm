from collections import deque
import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n, target = map(int, input().rstrip().split())
    queue = list(-int(i) for i in input().split())
    dq = deque()
    for i in range(n):
        dq.append((queue[i], i))

    queue.sort()
    queue = deque(queue)
    print_order = 1
    while dq:
        largest = queue.popleft() # 가장 큰 수
        for _ in range(n):
            if largest != dq[0][0]: # 중요도가 현재 가장 큰 수가 아니면 뒤로 넣기
                dq.rotate(-1)
            else:
                break

        num, idx = dq.popleft() # 가장 큰 수 pop

        if  idx == target:
            print(print_order)
            break
        else:
            print_order += 1
