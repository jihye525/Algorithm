s = input()
t = 0
for c in s:
    no = ord(c)
    if 65 <= no <= 90:
        if no <= 67:
            t += 3
        elif no <= 70:
            t += 4
        elif no <= 73:
            t += 5
        elif no <= 76:
            t += 6
        elif no <= 79:
            t += 7
        elif no <= 83:
            t += 8
        elif no <= 86:
            t += 9
        else:
            t += 10
print(t)
