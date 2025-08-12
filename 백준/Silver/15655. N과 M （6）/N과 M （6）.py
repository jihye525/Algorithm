
def recur(number):
    if number == M:
        print(*arr)
        return

    for i in lst:
        if arr and i <= arr[-1]:
            continue
        arr.append(i)
        recur(number + 1)
        arr.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
arr = []
recur(0)