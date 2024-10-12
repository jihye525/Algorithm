n = int(input())
lst = list(map(int, input().split()))
lst.sort()
time = [lst[0]]
for i in range(1, n):
    time.append(time[i-1] + lst[i])

print(sum(time))
