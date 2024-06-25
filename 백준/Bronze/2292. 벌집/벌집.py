def sol():
    n = int(input())
    nth = 0
    room = 1
    if n == 1:
        print(1)
        return
    while True:
        if room < n <= room + (6 * nth):
            print(nth + 1)
            break
        room += 6 * nth
        nth += 1

sol()