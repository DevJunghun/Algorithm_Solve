import sys

n = int(sys.stdin.readline())
wine_list = [0] + [ int(sys.stdin.readline()) for _ in range(n) ]

if n <= 2: print(sum(wine_list))
else:
  dp = [0] * (n + 1)
  dp[1] = wine_list[1]
  dp[2] = wine_list[1] + wine_list[2]

  for i in range(3, n + 1):
    dp[i] = max(dp[i], dp[i - 3] + wine_list[i - 1] + wine_list[i], dp[i - 2] + wine_list[i], dp[i - 1])

  print(dp[-1])