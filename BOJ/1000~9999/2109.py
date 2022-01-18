import sys
import heapq

n = int(sys.stdin.readline())
q = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ], key=lambda x: x[1])
price_list = []

for i in q:
  heapq.heappush(price_list, i[0])
  if len(price_list) > i[1]:
    heapq.heappop(price_list)

print(sum(price_list))
