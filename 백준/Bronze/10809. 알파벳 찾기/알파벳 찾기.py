s = input()
clst = []
for i in range(26):
    loc = s.find(chr(i+97))
    clst.append(str(loc))

print(" ".join(a for a in clst))