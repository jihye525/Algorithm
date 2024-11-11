import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    alpha = list(input().split())
    words = [alpha[0]]

    for i in range(1, n):
        temp = []
        for word in words:
            temp.append(min(word + alpha[i], alpha[i] + word))
        words = temp

    print(words[0])