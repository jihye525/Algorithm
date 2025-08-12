def recur(number):
    if number == M:
        print(*arr)
        return

    for i in lst:
        if i in arr:
            continue
        arr.append(i)
        recur(number + 1)
        arr.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
arr = []
recur(0)