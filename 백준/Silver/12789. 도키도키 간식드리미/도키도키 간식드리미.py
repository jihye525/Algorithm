n = int(input())
s = list(map(int, input().split()))
ans = []
i = 1
while True:
    if len(s) == 0:
        break
    if s[0] == i:
        s = s[1:]
        i += 1
    else:
        if len(ans) == 0 or ans[-1] != i:
            ans.append(s[0])
            s = s[1:]
        elif len(ans) and ans[-1] == i:
            while True:
                if len(ans) and ans[-1] == i:
                    ans.pop()
                    i += 1
                else:
                    break
if len(ans):
    while True:
        if len(ans) and ans[-1] == i:
            ans.pop()
            i += 1
        else:
            break

if len(s) or len(ans) or i != n+1:
    print("Sad")
else:
    print("Nice")