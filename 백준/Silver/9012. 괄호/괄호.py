n = int(input())
for _ in range(n):
    s = list(input())
    ans = []
    for c in s:
        if c == '(':
            ans.append(c)
        elif c == ')':
            if len(ans) != 0:
                ans.pop()
            else:
                ans.append(c)
                break

    if len(ans) == 0:
        print("YES")
    else:
        print("NO")