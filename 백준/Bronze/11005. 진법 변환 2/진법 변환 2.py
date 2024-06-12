n, b = map(int, input().split())
s = ""
while n:
    m = n % b
    if m < 10:
        s = str(m) + s
    else:
        s = chr(m + 55) + s
    n = n // b

print(s)