n = int(input())
dp = [0] * (n + 1)
if n <= 3: print(n)
else:
  for i in range(1, 4):
    dp[i] = i

  for i in range(4, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

  print(dp[n])