n_h, n_m, n_s = map(int, input().split(":"))
e_h, e_m, e_s = map(int, input().split(":"))
s, m, h = 0, 0, 0
if e_h > n_h:
    s = 60 + e_s - n_s
    m = 59 + e_m - n_m
    h = e_h - 1 - n_h
else:
    s = 60 - n_s + e_s
    m = 59 - n_m + e_m
    h = 23 - n_h + e_h

if s >= 60:
    s -= 60
    m += 1
if m >= 60:
    m -= 60
    h += 1
if h >= 24:
    h = 0

print("%02d:%02d:%02d" %(h, m, s))
