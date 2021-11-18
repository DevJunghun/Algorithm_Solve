from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())
deq = deque(range(1, a + 1))
res = list()

while deq:
    deq.rotate(-(b - 1))
    res.append(str(deq.popleft()))

print("<", ", ".join(res), ">", sep = '')