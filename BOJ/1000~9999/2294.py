import sys

n, k = map(int, sys.stdin.readline().split())
coin = [ int(sys.stdin.readline()) for _ in range(n) ]
dp = [ sys.maxsize ] * (k + 1)
dp[0] = 0

for c in coin:
  for i in range(c, k + 1):
    dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] != sys.maxsize:
  print(dp[k])
else:
  print(-1)