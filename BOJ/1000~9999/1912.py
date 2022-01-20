import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = num_list[0]
for i in range(1, n):
  dp[i] = max(dp[i - 1] + num_list[i], num_list[i])

print(max(dp))