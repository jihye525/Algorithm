t = int(input())

for _ in range(t):
    score_y, score_k = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        score_y += y
        score_k += k

    if score_y == score_k:
        print("Draw")
    elif score_y > score_k:
        print("Yonsei")
    elif score_y < score_k:
        print("Korea")