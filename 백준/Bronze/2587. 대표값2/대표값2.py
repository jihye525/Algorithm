lst = []
for _ in range(5):
    i = int(input())
    lst.append(i)

print(sum(lst)//5)
lst.sort()
print(lst[2])
    