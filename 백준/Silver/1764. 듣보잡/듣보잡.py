n, m = map(int, input().split())
notheard = set([])
notseen = set([])
for _ in range(n):
    notheard.update([input()])

for _ in range(m):
    notseen.update([input()])
lst = sorted(list(notheard & notseen))
print(len(lst))
for a in lst:
    print(a)