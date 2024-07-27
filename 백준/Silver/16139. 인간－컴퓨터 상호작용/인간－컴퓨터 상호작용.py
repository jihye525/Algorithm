import sys
input = sys.stdin.readline
str = input().rstrip()
chr_idx_lst = [[] for _ in range(26)]
n = int(input())
for i in range(len(str)):
    chr_idx_lst[ord(str[i])-97].append(i)
for _ in range(n):
    alpha, s, e = input().split()
    s, e = int(s), int(e)
    temp = chr_idx_lst[ord(alpha)-97]
    ans = 0
    for idx in temp:
        if s <= idx <= e:
            ans += 1
        elif idx > e:
            break
    print(ans)