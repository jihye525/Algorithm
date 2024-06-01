n1, n2 = map(int, input().split())
gcd = 0
m = min(n1, n2)
for i in range(m, 0, -1):
    if (n1 % i) == 0 and (n2 % i) == 0:
        gcd = i
        break

print(gcd)
print((n1 // gcd) * n2)