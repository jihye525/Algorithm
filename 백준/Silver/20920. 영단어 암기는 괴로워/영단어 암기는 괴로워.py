import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
dic = dict()
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

s1 = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for a in s1:
    print(a[0])