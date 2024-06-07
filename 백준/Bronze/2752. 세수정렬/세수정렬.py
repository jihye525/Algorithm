lst = list(map(int, input().split()))
lst.sort()
print(" ".join(str(a) for a in lst))