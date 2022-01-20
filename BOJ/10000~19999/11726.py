n = int(input())
dp = [0] * 1001
for i in range(1, 4):
  dp[i] = i
for i in range(4, len(dp)):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n] % 10007)