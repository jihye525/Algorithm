import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    p = [0] * (n + 1)

    for __ in range(n - 1):
        a, b = map(int, input().split())
        p[b] = a

    a, b = map(int, input().split())

    a_list = [0, a]
    b_list = [0, b]

    while p[a]:
        a_list.append(p[a])
        a = p[a]
    while p[b]:
        b_list.append(p[b])
        b = p[b]

    cnt = 1
    
    while a_list[-cnt] == b_list[-cnt]:
        cnt += 1

    print(a_list[-cnt + 1])