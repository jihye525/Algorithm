import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    circles = [tuple(map(int, input().split())) for _ in range(n)]

    intervals = [(x - r, x + r) for x, r in circles]
    intervals.sort()

    prev_start = -float('inf')
    prev_end = -float('inf')

    for start, end in intervals:
        if start < prev_end:# 겹치는 경우
            if prev_start < start and end < prev_end:# 원 안에 다른 원이 완전히 들어간 경우는 통과
                prev_start = start
                prev_end = end
                continue
            print("NO")
            return
        prev_start = start
        prev_end = end

    print("YES")

solve()