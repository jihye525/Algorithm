import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    order = input().strip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        arr = []

    reverse = 0
    error_flag = 0
    for f in order:
        if f == 'R':
            reverse = not reverse
        elif f == 'D':
            if not arr:
                print("error")
                error_flag = 1
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if not error_flag:
        if reverse:
            arr.reverse()
            print("["+",".join(arr)+"]")
        else:
            print("["+",".join(arr)+"]")