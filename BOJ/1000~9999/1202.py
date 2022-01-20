import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewelry_list = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ], key=lambda x: (x[0], x[1]))
bag_list = sorted([ int(sys.stdin.readline()) for _ in range(k) ])

price_sum = 0
q = []

for bag in bag_list:
  while jewelry_list and bag >= jewelry_list[0][0]:
    heapq.heappush(q, -jewelry_list[0][1])
    heapq.heappop(jewelry_list)

  if q: price_sum -= heapq.heappop(q)
  elif not jewelry_list: break    

print(price_sum)
