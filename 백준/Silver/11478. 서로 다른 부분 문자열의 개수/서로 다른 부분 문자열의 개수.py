s = input()
lst = []
for i in range(len(s)):
    for j in range(0, len(s)-i):
        lst.append(s[j:j+i+1])

ans = set(lst)
print(len(ans))