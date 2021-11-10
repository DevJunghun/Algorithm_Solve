import sys
from collections import deque

num = int(input())
for i in range(num):
    printer = list(map(int, sys.stdin.readline().split()))
    important = list(map(int, sys.stdin.readline().split()))
    
    deq = deque([(v, i) for i, v in enumerate(important)])
    count = 0
    while len(deq):
        j = deq.popleft()
        if deq and max(deq)[0] > j[0]: deq.append(j)
        else:
            count += 1
            if j[1] == printer[1]: break
    print(count)