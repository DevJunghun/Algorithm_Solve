import heapq
import sys

num = int(sys.stdin.readline())
q, count = list(), list()
for i in range(num):
    num, start, end = tuple(map(int, sys.stdin.readline().split()))
    heapq.heappush(q, (start, end, num))

start, end, num = heapq.heappop(q)
heapq.heappush(count, (end, start, num))

while q:
    start, end, num = heapq.heappop(q)
    if count[0][0] <= start:
        heapq.heappop(count)
    heapq.heappush(count, (end, start, num))
print(len(count))