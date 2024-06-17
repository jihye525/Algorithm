import sys
input = sys.stdin.readline
istr = input().strip()
lst = []
for i in range(len(istr)):
    lst.append(int(istr[i]))

lst.sort(reverse=True)

for i in lst:
    print(i, end="")