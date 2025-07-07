import sys

input = sys.stdin.readline

while True:
    str = input().rstrip()
    stack = ['.']

    if str == '.':
        break

    check = True

    for c in str:
        if c.isalpha() or c == " ":
            continue
        elif c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                if stack[-1] != '(':
                    check = False
                    break
                else:
                    stack.pop()
            else:
                check = False
                break

        elif c == '[':
            stack.append(c)
        elif c == ']':
            if stack:
                if stack[-1] != '[':
                    check = False
                    break
                else:
                    stack.pop()
            else:
                check = False
                break
        elif c == ".":
            if stack[-1] == ".":
                stack.pop()
            else:
                check = False
                break

    if check and len(stack) == 0:
        print("yes")
    else:
        print("no")