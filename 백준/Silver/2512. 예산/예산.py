import sys
input = sys.stdin.readline
n = int(input())
locals = list(map(int, input().split()))
national = int(input())
start = 0
end = max(locals)
ans = 0

while start <= end:
    mid = (start + end) // 2
    budget = 0
    for l in locals:
        if l < mid:
            budget += l
        else:
            budget += mid

    if budget > national:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)