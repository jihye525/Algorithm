import sys
input = sys.stdin.readline

n = int(input())
words = [input() for _ in range(n)]

check = dict()
for word in words:
    tmp = ''
    for char in word:
        tmp += char
        check[tmp] = check.get(tmp, 0) + 1

prefix, max_length = '', 0
for a, b in check.items():
    tmp_length = len(a)
    if b > 1:
        if tmp_length > max_length:
            prefix = a
            max_length = tmp_length

cnt = 0
for word in words:
    if prefix == word[:max_length]:
        cnt += 1
        print(word, end="")
    if cnt == 2:
        break