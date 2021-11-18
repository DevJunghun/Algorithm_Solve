from collections import deque

def solution(priorities, location):
    deq = deque([(v, i) for i, v in enumerate(priorities)])
    count = 0
    while len(deq):
        j = deq.popleft()
        if deq and max(deq)[0] > j[0]: deq.append(j)
        else:
            count += 1
            if j[1] == location:
                break
            
    return count