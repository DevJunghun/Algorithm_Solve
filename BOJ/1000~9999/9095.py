import sys

t = int(sys.stdin.readline())
num_list = [ int(sys.stdin.readline()) for _ in range(t) ]
for i in num_list:
  dp = [0] * max(4, (i + 1))
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4
  for j in range(4, i + 1):
    dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

  print(dp[i])