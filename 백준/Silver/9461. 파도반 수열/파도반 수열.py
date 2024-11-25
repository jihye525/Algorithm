tc = int(input())
n_lst = [int(input()) for _ in range(tc)]
dp = [1, 1, 1, 2, 2] + [0] * (max(n_lst))
for i in range(5, max(n_lst)):
    dp[i] = dp[i - 1] + dp[i - 5]

for n in n_lst:
    print(dp[n-1])
    
    