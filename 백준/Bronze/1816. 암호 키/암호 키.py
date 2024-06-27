n = int(input())
for _ in range(n):
    num = int(input())
    is_prime = 1
    for i in range(2, 1000001):
        if num % i == 0:
            is_prime = 0
            print("NO")
            break
    if is_prime:
        print("YES")