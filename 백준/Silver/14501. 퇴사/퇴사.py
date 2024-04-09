import sys

read = sys.stdin.readline

n = int(read())
TP = [list(map(int, read().split())) for _ in range(n)]

sumList = [0] * (n + 1)  # 맨 마지막은 0으로 초기화

for i in range(n-1, -1, -1): #마지막부터 앞으로
    if i + TP[i][0] <= n:
        if sumList[i + TP[i][0]] + TP[i][1] >= sumList[i + 1]:
            sumList[i] = sumList[i+TP[i][0]] + TP[i][1]
        else:
            sumList[i] = sumList[i + 1]
    else:
        sumList[i] = sumList[i + 1]

print(sumList[0])