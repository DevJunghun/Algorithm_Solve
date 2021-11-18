from collections import deque

num = int(input())
deq = deque(list(range(1, num + 1)))
while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])