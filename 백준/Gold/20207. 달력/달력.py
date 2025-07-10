import sys

input = sys.stdin.readline

n = int(input())
calendar_list = [0] * 367

for i in range(n):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        calendar_list[j] += 1

max_num = 0
width = 0
paper = 0
for i in range(1, 367):
    if calendar_list[i] > 0:
        width += 1
        if max_num < calendar_list[i]:
            max_num = calendar_list[i]

    if calendar_list[i] == 0 and max_num > 0 and width > 0:
        paper += width * max_num
        width, max_num = 0, 0

print(paper)