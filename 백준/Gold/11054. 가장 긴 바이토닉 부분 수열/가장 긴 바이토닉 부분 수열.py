n = int(input())
lst = list(map(int, input().split()))
reverse_lst = lst[::-1]
dp_up = [1 for _ in range(n)]
dp_down = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)
        if reverse_lst[j] < reverse_lst[i]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)


print(max([dp_up[i] + dp_down[n-1-i] for i in range(n)]))
