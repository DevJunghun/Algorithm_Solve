import sys
import heapq

n = int(sys.stdin.readline())
lecture_list = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ], key=lambda x: (x[0], x[1]))
room_list = []
heapq.heappush(room_list, lecture_list[0][1])

for i in range(1, n):
  if lecture_list[i][0] < room_list[0]:
    heapq.heappush(room_list, lecture_list[i][1])
  else:
    heapq.heappop(room_list)
    heapq.heappush(room_list, lecture_list[i][1])

print(len(room_list))