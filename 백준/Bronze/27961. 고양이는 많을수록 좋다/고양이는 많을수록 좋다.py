n = int(input())
cats = 1
magic = 1
while cats * 2 < n:
    cats *= 2
    magic += 1

if n <= 1:
    print(n)
else:
    print(magic + 1)