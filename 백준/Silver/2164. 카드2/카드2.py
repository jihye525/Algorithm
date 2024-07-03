from collections import deque

n = int(input())
d = deque([i for i in range(1, n + 1)])
while True:
    if len(d) == 1:
        print(d[0])
        break

    d.popleft()
    d.append(d.popleft())