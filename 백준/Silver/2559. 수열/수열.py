import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [lst[0]]
for i in range(1, n):
    sum_lst.append(sum_lst[i-1] + lst[i])
M = sum_lst[m-1]
for j in range(1, n-m+1):
    temp = sum_lst[j + m - 1] - sum_lst[j - 1]
    if temp > M:
        M = temp

print(M)