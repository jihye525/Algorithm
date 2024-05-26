while True:
    n = int(input())
    if n == -1:
        break
    
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)

    if sum(lst) == n:
        s = str(n) + " = "
        for c in lst:
            s += str(c) + " + " 
        print(s[:-3])
    else:
        print(f"{n} is NOT perfect.")
    