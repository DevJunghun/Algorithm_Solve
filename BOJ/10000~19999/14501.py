import sys

n = int(sys.stdin.readline())
c_list = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ]
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
  if c_list[i][0] + i > n: dp[i] = dp[i + 1]
  else: dp[i] = max(dp[i + 1], dp[i + c_list[i][0]] + c_list[i][1])
print(dp[0])