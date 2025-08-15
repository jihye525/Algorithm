import sys
input = sys.stdin.readline

n = int(input())
interviews = [list(map(int, input().split())) for _ in range(n)]
dp = [-1 for _ in range(n + 1)]

def recur(idx):
    if idx == n:
        return 0
    if idx > n:
        return -9999999999999

    if dp[idx] != -1:
        return dp[idx]

    #상담을 받거나 안받거나 중 더 이득인 것을 dp에 저장시키기
    dp[idx] = max(recur(idx + interviews[idx][0]) + interviews[idx][1], recur(idx + 1))

    return dp[idx]

recur(0)
print(dp[0])