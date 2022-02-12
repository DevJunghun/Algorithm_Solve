n = int(input())
dp = [1] * (1010)
dp[0] = 0
for i in range(2, 1010):
  dp[i] = (dp[i - 1] * i)

print(dp[n + 9] // (dp[9] * dp[n]) % 10007)
