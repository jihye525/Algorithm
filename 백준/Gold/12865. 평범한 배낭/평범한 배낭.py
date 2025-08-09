import sys
input = sys.stdin.readline

noo, js_weight = map(int, input().split())
objects = [tuple(map(int, input().split())) for _ in range(noo)]

dp = [0] * (js_weight + 1)  # dp[w] = 무게 w일 때 최대 가치

for w, v in objects:
    for weight in range(js_weight, w - 1, -1):  # 뒤에서 앞으로 순회
        dp[weight] = max(dp[weight], dp[weight - w] + v)

print(dp[js_weight])