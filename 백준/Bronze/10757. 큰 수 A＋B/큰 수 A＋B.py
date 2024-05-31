
n1, n2 = input().split()
tmp = 0
ans = ""
hap = 0
M = max(len(n1), len(n2))
if len(n1) > len(n2):
    n2 = "0" * (M - len(n2)) + n2
    left_end = int(n1[0])
elif len(n1) == len(n2):
    n1 = "0" * (M - len(n1)) + n1
    left_end = int(n1[0]) +int(n2[0])
else:
    n1 = "0" * (M - len(n1)) + n1
    left_end = int(n2[0])

for i in range(1, M):
    if tmp != 0:
        hap = int(n1[-i]) + int(n2[-i]) + tmp
        tmp = 0
    else:
        hap = int(n1[-i]) + int(n2[-i])

    if hap > 9:
        tmp = hap // 10
        ans = str(hap % 10) + ans
    else:
        ans = str(hap) + ans

if tmp != 0 :
    left_end += tmp

print(str(left_end)+ans)