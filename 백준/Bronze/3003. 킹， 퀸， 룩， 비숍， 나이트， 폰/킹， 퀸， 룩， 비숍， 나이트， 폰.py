lst = [1, 1, 2, 2, 2, 8]

n_cnt = list(map(int, input().split()))
s = ""
for i in range(6):
    s += str(lst[i] - n_cnt[i]) + " "

print(s[:-1])