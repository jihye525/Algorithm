a, b, v = map(int, input().split())
if a - b < a:
    d = v // (a - b) - a - 2
    v -= (a - b) * d
else:
    d = v // a
    v -= (a-b) * d
while True:
    d += 1
    v -= a
    if v <= 0:
        break
    v += b

print(d)