t = int(input())
score_cy, score_js = 100, 100

for _ in range(t):
    cy, js = map(int, input().split())

    if cy == js:
        continue
    elif cy > js:
        score_js -= cy
    elif cy < js:
        score_cy -= js

print(score_cy)
print( score_js)