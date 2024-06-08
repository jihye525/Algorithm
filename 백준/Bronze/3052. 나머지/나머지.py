lst = []
for i in range(10):
    n = int(input())
    if (n % 42) not in lst:
        lst.append(n%42)
print(len(lst))