n = int(input())
s = 4
for i in range(1, n + 1):
    rc = (2**(i-1)) - 1
    s += (5 + (4 * rc)) + (rc * (4 + 3 * rc))
print(s)
