t = int(input())
lst = [0] * 5
for _ in range(t):
    x, y = map(int, input().split())
    if x and y:
        if x > 0 and y > 0:
            lst[1] += 1
        elif x < 0 and y > 0:
            lst[2] += 1
        elif x < 0 and y < 0:
            lst[3] += 1
        else:
            lst[4] += 1
    else:
        lst[0] += 1
        
print(f"Q1: {lst[1]}")
print(f"Q2: {lst[2]}")
print(f"Q3: {lst[3]}")
print(f"Q4: {lst[4]}")
print(f"AXIS: {lst[0]}")