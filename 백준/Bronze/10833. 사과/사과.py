school = int(input())
remain = 0
for _ in range(school):
    std, apple = map(int, input().split())
    remain += apple % std
    
print(remain)
        