import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
dp = [ -sys.maxsize for _ in range(m + 1) ]

for i in range(n - 1, -1, -1):
    room_number = p[i]
    for j in range(room_number, m + 1):
        dp[j] = max(dp[j - room_number] * 10 + i, i, dp[j])

print(dp[m])