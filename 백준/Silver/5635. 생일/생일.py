n = int(input())
oldest = ["", 4, 6, 2024]
youngest = ["", 1, 1, 0]
for i in range(n):
    name, dd, mm, year = input().split()
    dd, mm, year = int(dd), int(mm), int(year)
    if year > youngest[3]:
        youngest = [name, dd, mm, year]
    elif year == youngest[3]:
        if mm > youngest[2]:
            youngest = [name, dd, mm, year]
        elif mm == youngest[2]:
            if dd > youngest[1]:
                youngest = [name, dd, mm, year]

    if year < oldest[3]:
        oldest = [name, dd, mm, year]
    elif year == oldest[3]:
        if mm < oldest[2]:
            oldest = [name, dd, mm, year]
        elif mm == oldest[2]:
            if dd < oldest[1]:
                oldest = [name, dd, mm, year]

print(youngest[0])
print(oldest[0])