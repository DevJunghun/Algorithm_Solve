import sys
import heapq

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor_list = sorted(list(map(int, sys.stdin.readline().split())))

if k >= n: print(0)
else:
  q = []
  for i in range(1, n):
    heapq.heappush(q, -(sensor_list[i] - sensor_list[i - 1]))
  for i in range(k - 1):
    heapq.heappop(q)
  print(-sum(q))