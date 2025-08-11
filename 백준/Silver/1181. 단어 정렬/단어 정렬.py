import sys
input = sys.stdin.readline

n = int(input())
words = set(input().strip() for _ in range(n))
words = list((len(i), i) for i in words)
words.sort(key=lambda w: (w[0], w[1]))
for w in words:
    print(w[1])