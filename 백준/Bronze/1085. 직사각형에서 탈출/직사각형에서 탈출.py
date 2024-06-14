x, y, w, h = map(int, input().split())
lst = [x, y, abs(w-x), abs(y-h)]
print(min(lst))