t = int(input())

if t % 10 != 0:
    print(-1)
else:
    d_300 = t // 300
    t = t % 300
    d_100 = t // 60
    t = t % 60
    d_10 = t // 10

    print(d_300, d_100, d_10)