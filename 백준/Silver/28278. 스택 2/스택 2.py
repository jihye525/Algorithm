import sys

stk = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = sys.stdin.readline()
    len_of_stack = len(stk)
    if x[0] == '1':
        a, X = map(int, x.split())
        stk.append(X)
    elif x[0] == '2':
        if not len_of_stack:
            print(-1)
        else:
            print(stk.pop())
    elif x[0] == '3':
        print(len_of_stack)
    elif x[0] == '4':
        if not len_of_stack:
            print(1)
        else:
            print(0)
    elif x[0] == '5':
        if not len_of_stack:
            print(-1)
        else:
            print(stk[-1])