import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
dic = {}
for i in range(1, n + 1):
    a = input().rstrip()
    dic[a] = i
    dic[str(i)] = a


for _ in range(m):
    q = input().rstrip()
    print(dic[q])