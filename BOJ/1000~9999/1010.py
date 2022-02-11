import sys

t = int(sys.stdin.readline())
for _ in range(t):
  west, east = map(int, sys.stdin.readline().split())
  dp = [1] * 31
  for i in range(1, 31):
    dp[i] = dp[i - 1] * i
  
  print(dp[east] // (dp[west] * dp[east - west]))