import sys

n = int(sys.stdin.readline())
balloon_list = list(map(int, sys.stdin.readline().split()))
check = [0] * (1000001)
arrow_count = 0

for b in balloon_list:
  if check[b] == 0:
    arrow_count += 1
    check[b - 1] += 1
  
  elif check[b] > 0:
    check[b] -= 1
    check[b - 1] += 1

print(arrow_count)