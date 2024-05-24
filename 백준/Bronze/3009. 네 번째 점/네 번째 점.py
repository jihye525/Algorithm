x_lst = []
y_lst = []

for _ in range(3):
    x, y = input().split()
    if x in x_lst:
        x_lst.remove(x)
    else:
        x_lst.append(x) 
    if y  in y_lst:
        y_lst.remove(y)
    else:
        y_lst.append(y)
        
print(x_lst[0], y_lst[0])