import sys
input = sys.stdin.readline

string = input().strip()
stack = []

for i in string:
    if i == '(' or i == '[':
        stack.append(i)
    elif i == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if temp == 0 else 2 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)

    elif i == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if temp == 0 else 3 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)

ans = 0
for s in stack:
    if isinstance(s, int):
        ans += s
    else:
        print(0)
        exit(0)

print(ans)