lst = []

for _ in range(7):
    a = int(input())
    if a % 2 == 1:
        lst.append(a)
        
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))