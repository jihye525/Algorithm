n = int(input())
s_idx = 1
e_idx = 1
s = 1
cnt = 1
while e_idx != n:
    if s == n:
        cnt += 1
        e_idx += 1
        s += e_idx
    elif s < n:
        e_idx += 1
        s += e_idx
    else:
        s -= s_idx
        s_idx += 1
        
print(cnt)
      