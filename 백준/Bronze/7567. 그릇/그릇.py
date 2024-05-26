lst = input()
h = 10

for i in range(1, len(lst)):
    if lst[i-1] == "(" and lst[i] == "(":
        h += 5
    elif lst[i-1] == "(" and lst[i] == ")":
        h += 10
    elif lst[i-1] == ")" and lst[i] == ")":
        h += 5
    elif lst[i-1] == ")" and lst[i] == "(":
        h += 10

print(h)