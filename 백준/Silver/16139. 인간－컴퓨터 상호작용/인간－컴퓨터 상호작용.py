import sys
input = sys.stdin.readline
str = input().rstrip()
n = int(input())
chr_total_lst = [[0] * 26]

chr_total_lst[0][ord(str[0])-97] = 1

for i in range(1, len(str)):
    c = ord(str[i])-97
    temp = chr_total_lst[i-1].copy()
    temp[c] = chr_total_lst[i-1][c] + 1
    chr_total_lst.append(temp)

for _ in range(n):
    alpha, s, e = input().split()
    s, e = int(s), int(e)
    if s == 0:
        print(chr_total_lst[e][ord(alpha)-97])
    else:
        print(chr_total_lst[e][ord(alpha)-97]-chr_total_lst[s-1][ord(alpha)-97])
        