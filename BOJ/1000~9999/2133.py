n = int(input())
if n % 2 != 0: print(0)
else:
  n = n // 2
  dp = [0] * (n + 1)
  dp[0] = 0
  dp[1] = 3
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] * dp[1] + sum(dp[:i - 1]) * 2 + 2

  print(dp[n])