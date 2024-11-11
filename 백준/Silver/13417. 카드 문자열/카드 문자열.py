import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    alpha = list(input().split())
    first_word = ""

    for i in range(n):
        first_word = min(first_word + alpha[i], alpha[i] + first_word)

    print(first_word)