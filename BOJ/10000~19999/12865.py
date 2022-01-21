import sys

n, k = map(int, sys.stdin.readline().split())
things_list = [(0, 0)] + [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ]
dp = [ [ 0 for _ in range(k + 1) ] for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    w = things_list[i][0]
    v = things_list[i][1]

    if j < w: dp[i][j] = dp[i - 1][j]
    else: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[-1][-1])