def get_spiral_number(x, y):
    layer = max(abs(x), abs(y))
    max_value = (2 * layer + 1) ** 2
    
    if x == layer:
        return max_value - (layer - y)
    max_value -= 2 * layer
    if y == -layer:
        return max_value - (layer - x)
    max_value -= 2 * layer
    if x == -layer:
        return max_value - (layer + y)
    max_value -= 2 * layer
    return max_value - (layer + x)

def print_spiral_partial(r1, c1, r2, c2):
    max_num = max(get_spiral_number(r1, c1), get_spiral_number(r1, c2),
                   get_spiral_number(r2, c1), get_spiral_number(r2, c2))
    width = len(str(max_num))
    
    for i in range(r1, r2 + 1):
        print(" ".join(f"{get_spiral_number(i, j):>{width}}" for j in range(c1, c2 + 1)))

r1, c1, r2, c2 =map(int, input().split())
print_spiral_partial(r1, c1, r2, c2)