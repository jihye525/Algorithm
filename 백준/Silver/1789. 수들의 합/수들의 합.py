N = int(input())
s = 0
cnt = 0
while True:
    cnt += 1
    s += cnt
    if s > N:
        break
    
print(cnt-1)