import sys

n = int(sys.stdin.readline())
time_list = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ]
time_list.sort(key=lambda x: x[1], reverse=True)

min_start_time = time_list[0][1] - time_list[0][0]
for i in range(1, n):
  temp = time_list[i][1] - time_list[i][0]
  if min_start_time > time_list[i][1]:
    min_start_time = temp
  else:
    min_start_time -= time_list[i][0]

print(min_start_time if min_start_time >= 0 else -1)