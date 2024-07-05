n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
for i in range(n):
    s_idx = 0
    e_idx = n - 1
    while s_idx < e_idx:
        if lst[s_idx] + lst[e_idx] == lst[i]:
            if s_idx == i:
                s_idx += 1
            elif e_idx == i:
                e_idx -= 1
            else:
                cnt += 1
                break
        elif lst[s_idx] + lst[e_idx] < lst[i]:
            s_idx += 1
        else:
            e_idx -= 1

print(cnt)            
    