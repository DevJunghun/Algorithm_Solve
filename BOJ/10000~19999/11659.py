import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0] * (n + 1)

for i in range(1, n + 1):
    sum_list[i] = sum_list[i - 1] + num_list[i - 1]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i - 1])