t = int(input())
for _ in range(t):
    ox = input()
    pnt = 0 
    s = 0
    for c in ox:
        if c == "O":
            pnt += 1
            s += pnt
        elif c == "X":
            pnt = 0
    print(s)