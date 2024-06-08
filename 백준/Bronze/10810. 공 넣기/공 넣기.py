n, m = map(int, input().split())
lst = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    lst = lst[:i-1] + [k] * (j - i + 1) + lst[j:]

print(" ".join(map(str, lst)))