import sys
import heapq

n = int(sys.stdin.readline())
homework_list = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ], key=lambda x: (x[0], x[1]))
q = []
score = 0
last_day = homework_list[-1][0]

while last_day != 0:
  while homework_list and homework_list[-1][0] >= last_day:
    heapq.heappush(q, -homework_list.pop()[1])
  last_day -= 1

  if not q: continue
  score -= heapq.heappop(q)

print(score)