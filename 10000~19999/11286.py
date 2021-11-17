import heapq
import sys

num = int(sys.stdin.readline())
heap = list()
for i in range(num):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap) == 0: print(0)
        else: print(heapq.heappop(heap)[1])
    
    else: heapq.heappush(heap, (abs(data), data))
