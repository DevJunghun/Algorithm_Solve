import sys

t = int(sys.stdin.readline())
for i in range(t):
  tree_num = int(sys.stdin.readline())
  height_list = sorted(list(map(int, sys.stdin.readline().split())))
  max_height = 0
  for i in range(2, tree_num):
    max_height = max(max_height, abs(height_list[i] - height_list[i - 2]))
  
  print(max_height)