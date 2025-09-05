import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = list(input().rstrip())
stack = []
count = 0
for i in range(n):
    while stack and stack[-1] < number[i] and count < k:
        stack.pop()
        count += 1
    stack.append(number[i])

while count < k:
    stack.pop()
    count += 1

print("".join(stack))

