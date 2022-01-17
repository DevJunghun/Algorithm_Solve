import sys
import heapq

num = int(sys.stdin.readline())
problem_list = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(num) ])
cup_list = []
deadline = 0

for p in problem_list:
  deadline = p[0]
  heapq.heappush(cup_list, p[1])

  while len(cup_list) > deadline:
    heapq.heappop(cup_list)
    
print(sum(cup_list))