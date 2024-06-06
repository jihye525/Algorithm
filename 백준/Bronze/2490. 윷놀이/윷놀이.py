for _ in range(3):
    lst = list(map(int, input().split()))
    s = lst.count(1)
    if s == 3:
        print("A")
    elif s == 2:
        print("B")
    elif s == 1:
        print("C")
    elif s == 0:
        print("D")
    elif s == 4:
        print("E")