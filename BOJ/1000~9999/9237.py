import sys

n = int(sys.stdin.readline())
tree_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
day, idx = 1, 0
while idx < n:
  tree_list[idx] = tree_list[idx] + day
  day += 1
  idx += 1
print(max(tree_list) + 1)