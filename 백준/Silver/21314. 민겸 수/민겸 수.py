import sys
input = sys.stdin.readline
string = input().rstrip()
max_v, min_v = '', ''
m = 0
for i in range(len(string)):
    if string[i] == 'M':
        m += 1
    elif string[i] == 'K':
        if m > 0:
            max_v += str(5 * (10 ** m))
            min_v += str(10 ** m + 5)
        else:
            max_v += '5'
            min_v += '5'
        m = 0

if m > 0:
    for i in range(m):
        max_v += '1'
    min_v += str(10 ** (m - 1))

print(max_v)
print(min_v)