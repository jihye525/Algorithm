n, m = map(int, input().split())
lst = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        lst = lst[:i-1]+lst[j-1::-1]+lst[j:]
    else:
        lst = lst[:i-1]+lst[j-1:i-2:-1]+lst[j:]

print(" ".join(map(str, lst)))