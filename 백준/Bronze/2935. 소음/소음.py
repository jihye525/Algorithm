n1 = input().count('0')
opr = input()
n2 = input().count('0')
ans = ""

if opr == "+":
    if n1 == n2:
        ans += '2'
        ans += '0' * n1
    else:
        M = max(n1, n2)
        m = min(n1, n2)
        for i in range(0, M):
            if i == m:
                ans = '1' + ans
                continue
            ans = '0' + ans
        ans = '1' + ans

if opr == "*":
    ans += '1'
    for _ in range(n1 + n2):
        ans += '0'

print(ans)
