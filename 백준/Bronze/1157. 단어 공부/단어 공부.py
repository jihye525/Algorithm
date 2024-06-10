s = input()
clst = []
for i in range(26):
    cnt = s.count(chr(i+97))+s.count(chr(i+65))
    clst.append(cnt)

M = max(clst)
if clst.count(M) > 1:
    print("?")
else:
    print(chr(clst.index(M)+65))