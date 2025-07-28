import sys
input = sys.stdin.readline
lst = input().rstrip()
sticks = 0
ans = 0
for i in range(1, len(lst)):
    if lst[i-1:i+1] == "()":
        ans += sticks
    elif lst[i-1:i+1] == "((":
        sticks += 1
    elif lst[i-1:i+1] == "))":
        sticks -= 1
        ans += 1

print(ans)