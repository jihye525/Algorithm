def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a // gcd(a, b) * b

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
m = lcm(b1, b2)
s = (a1 * (m // b1)) + (a2 * (m // b2))

if gcd(s, m) == 1:
    print(s, m)
else:
    print(s // gcd(s, m), m // gcd(s, m))