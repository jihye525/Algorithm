n, b = input().split()
b = int(b)
m = 0
s = 0
for i in range(len(n)-1, -1, -1):
    if n[i].isdigit():
        s += int(n[i]) * (b ** m)
    elif n[i].isalpha():
        s += (ord(n[i]) - 55) * (b ** m)
    m += 1

print(s)