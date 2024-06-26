import sys, math

prime_arr = [0] * (2 * 123456 + 1)
prime_arr[0] = prime_arr[1] = 0
prime_arr[2] = 1
s = 1
for i in range(3, len(prime_arr)):
    is_prime = 1
    for j in range(2, int(math.sqrt(i))+2):
        if i % j == 0:
            is_prime = 0
            break
    if is_prime:
        s += 1

    prime_arr[i] = s

lst = list(map(int, sys.stdin.readlines()))
for i in range(len(lst)-1):
    print(prime_arr[lst[i] * 2] - prime_arr[lst[i]])