while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    lst = [a, b, c]
    lst.sort()
    if lst[2] >= lst[0] + lst[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b and b != c and a != c:
        print("Scalene")
