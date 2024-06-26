import math

t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 2:
        print(2)
        continue

    while True:
        is_prime = 1
        for i in range(2, int(math.sqrt(n)) + 2):
            if n % i == 0:
                is_prime = 0
                break

        if is_prime:
            print(n)
            break
        n += 1