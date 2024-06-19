import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
s = sorted(set(lst))
dic = {s[i]:i for i in range(len(s))}

for i in lst:
    print(dic[i], end=" ")