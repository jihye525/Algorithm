t = int(input())
lst = []

for _ in range(t):
    age, name = input().split()
    age = int(age)
    lst.append((age, name))

lst.sort(key= lambda x:x[0])

for a, n in lst:
    print(a, n)