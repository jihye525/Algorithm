import sys
si = sys.stdin.read().split()

for i in range(15):
    for j in range(5):
        if i < len(si[j]):
            print(si[j][i], end='')