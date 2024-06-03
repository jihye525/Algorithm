istr = input()
cnt = 0
while len(istr) > 0:
    if istr[0:2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        cnt += 1
        istr = istr[2:]
    elif istr[0:3] == "dz=":
        cnt += 1
        istr = istr[3:]
    else:
        cnt += 1
        istr = istr[1:]

print(cnt)
