import sys
from collections import deque
q = deque([])

tc = int(sys.stdin.readline())
l = 0
for _ in range(tc):
    opr = list(map(int, sys.stdin.readline().split()))
    if opr[0] == 1:
        q.appendleft(opr[1])
        l += 1
    elif opr[0] == 2:
        q.append(opr[1])
        l += 1
    elif opr[0] == 3:
        if l:
            print(q.popleft())
            l -= 1
        else:
            print(-1)
    elif opr[0] == 4:
        if l:
            print(q.pop())
            l -= 1
        else:
            print(-1)
    elif opr[0] == 5:
        print(l)
    elif opr[0] == 6:
        if l:
            print(0)
        else:
            print(1)
    elif opr[0] == 7:
        if l:
            print(q[0])
        else:
            print(-1)
    elif opr[0] == 8:
        if l:
            print(q[-1])
        else:
            print(-1)