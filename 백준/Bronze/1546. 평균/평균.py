n = int(input())
lst = list(map(int, input().split()))
M = max(lst)
s = 0
for a in lst:
    s += a / M * 100
    
print(s / n)