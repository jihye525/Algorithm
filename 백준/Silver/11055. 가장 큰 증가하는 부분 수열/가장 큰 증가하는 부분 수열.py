n = int(input())
nums = list(map(int, input().split()))
dp = nums.copy()
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+nums[i])
print(max(dp))
