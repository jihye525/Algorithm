lst = []
for i in range(10000):
    j = sum(map(int, str(i))) + i
    lst.append(j)

for i in range(1, 10001):
    if i not in lst:
        print(i)