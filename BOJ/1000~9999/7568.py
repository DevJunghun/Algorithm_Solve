import sys

n = int(sys.stdin.readline())
wh_list = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
for i in range(len(wh_list)):
  rank = 1
  for j in range(len(wh_list)):
    if wh_list[i][0] < wh_list[j][0] and wh_list[i][1] < wh_list[j][1]:
      rank += 1
  wh_list[i].append(rank)

for i in wh_list:
  print(i[2], end=" ")