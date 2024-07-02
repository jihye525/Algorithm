while True:
    s = input()
    if len(s) == 1 and s == '.':
        break
    ans = ['.']
    for c in s:
        if c.isalpha() or c == " ":
            continue
        elif c == '(':
            ans.append(c)
        elif c == ')':
            if len(ans) != 0:
                if ans[-1] == "(":
                    ans.pop()
                else:
                    break
            else:
                ans.append(c)
                break
        elif c == '[':
            ans.append(c)
        elif c == ']':
            if len(ans) != 0:
                if ans[-1] == "[":
                    ans.pop()
                else:
                    break
            else:
                ans.append(c)
                break
        elif c == '.':
            if ans[-1] == '.':
                ans.pop()

    if len(ans) == 0:
        print("yes")
    else:
        print("no")
