t = int(input())

for _ in range(t):
    r, e, c = map(int, input().split())
    profit = e - c - r
    
    if profit > 0:
        print("advertise")
    elif profit == 0:
        print("does not matter")
    else:
        print("do not advertise")