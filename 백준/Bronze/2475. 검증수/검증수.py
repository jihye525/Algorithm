lst = list(map(int, input().split()))
s = 0
for n in lst:
    s += n ** 2
    
print(s % 10)