import sys

n = int(sys.stdin.readline())
color_list = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

for i in range(1, n):
  color_list[i][0] += min(color_list[i - 1][1], color_list[i - 1][2])
  color_list[i][1] += min(color_list[i - 1][0], color_list[i - 1][2])
  color_list[i][2] += min(color_list[i - 1][0], color_list[i - 1][1])

print(min(color_list[-1]))