import sys

n = int(sys.stdin.readline())
floor_list = [0] + [ int(sys.stdin.readline()) for _ in range(n) ]

if n <= 2: print(sum(floor_list))
else:
  dp = [0] * (n + 1)
  dp[1] = floor_list[1]
  dp[2] = floor_list[1] + floor_list[2]

  for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + floor_list[i - 1] + floor_list[i], dp[i - 2] + floor_list[i])
  print(dp[-1])