min_edge = int(input())
max_edge = int(input())
n = 1
target = 1
lst = []
while max_edge >= target:
    if min_edge <= target:
        lst.append(target)
    n += 1
    target = n ** 2
    
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
