import sys

n = int(sys.stdin.readline())
for i in range(n):
  p = int(sys.stdin.readline())
  dp = [0] * 101
  dp[1] = 1
  dp[2] = 1
  dp[3] = 1
  for j in range(3, 101):
    dp[j] = dp[j - 3] + dp[j - 2]
  
  print(dp[p])