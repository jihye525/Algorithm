n = int(input())
a = []
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        a.append(i)
        n //= i

if n != 1:
    a.append(n)
print(len(a))
print(*a)