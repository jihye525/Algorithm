k = int(input())
stk = []
for _ in range(k):
    n = int(input())
    if n:
        stk.append(n)
    else:
        stk.pop()
        
print(sum(stk))