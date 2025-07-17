from collections import deque
import sys

read = sys.stdin.readline
n = int(read())
numbers = list(map(int, read().split()))
opr = list(map(int, read().split()))
ans = []


def dfs(rst, lst, opr):

    if len(lst) == 0:  
        ans.append(rst)
    else:
        if opr[0] != 0:
            oprC = opr.copy()
            oprC[0] -= 1
            dfs(rst + lst[0], lst[1:], oprC)

        if opr[1] != 0:
            oprC = opr.copy()
            oprC[1] -= 1
            dfs(rst - lst[0], lst[1:], oprC)

        if opr[2] != 0:
            oprC = opr.copy()
            oprC[2] -= 1
            dfs(rst * lst[0], lst[1:], oprC)

        if opr[3] != 0:
            oprC = opr.copy()
            oprC[3] -= 1
            dfs(int(rst / lst[0]), lst[1:], oprC)


dfs(numbers[0], numbers[1:], opr)

print(max(ans))
print(min(ans))