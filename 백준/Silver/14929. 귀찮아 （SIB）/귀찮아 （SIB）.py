import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

def solve():
    total = sum(arr)
    squares = sum(x * x for x in arr)
    S = (total * total - squares) // 2
    print(S)

solve()