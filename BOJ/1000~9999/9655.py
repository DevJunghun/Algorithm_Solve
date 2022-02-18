n = int(input())
dp = [-1] * 1001
for i in range(1, 4):
  if i % 2 != 0: dp[i] = 1
  else: dp[i] = 0
for i in range(4, n + 1):
  if dp[i - 1] or dp[i - 3]: dp[i] = 0
  else: dp[i] = 1

print("SK" if dp[n] != 0 else "CY")