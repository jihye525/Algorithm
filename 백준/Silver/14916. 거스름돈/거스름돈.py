n = int(input())
exchange_5 = n // 5
exchange_2 = n % 5 // 2
remain = n % 5 % 2

if remain != 0:
    for i in range(exchange_5, -1, -1):
        exchange_2 = (n - (i * 5)) // 2
        remain = (n - (i * 5)) % 2
        if remain == 0:
            exchange_5 = i
            break

if remain:
    print(-1)
else:
    print(exchange_5+exchange_2)
