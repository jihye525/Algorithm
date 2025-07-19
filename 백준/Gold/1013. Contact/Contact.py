import re
n = int(input())
p = re.compile('(100+1+|01)+')
for _ in range(n):
    string = input().rstrip()
    if p.fullmatch(string):
        print("YES")
    else:
        print("NO")
