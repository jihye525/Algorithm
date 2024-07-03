import sys
from collections import deque
q = deque([])
tc = int(sys.stdin.readline())
l = 0
for _ in range(tc):
    opr = sys.stdin.readline().split()
    if opr[0] == "push":
        q.append(opr[1])
        l += 1
    elif opr[0] == "pop":
        if len(q):
            print(q.popleft())
            l -= 1
        else:
            print(-1)
    elif opr[0] == "size":
        print(l)
    elif opr[0] == "empty":
        if l:
            print(0)
        else:
            print(1)
    elif opr[0] == "front":
        if l:
            print(q[0])
        else:
            print(-1)
    elif opr[0] == "back":
        if l:
            print(q[-1])
        else:
            print(-1)