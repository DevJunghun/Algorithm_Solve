import sys

n = int(sys.stdin.readline())
card = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
  for j in range(1, i + 1):
    dp[i] = max(dp[i], card[j] + dp[i - j])

print(dp[-1])