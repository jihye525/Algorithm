def recur(number, idx):
    if number == M:
        print(*arr)
        return

    for i in range(idx, len(lst)):
        arr.append(lst[i])
        recur(number + 1, i+1)
        arr.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
arr = []
recur(0, 0)