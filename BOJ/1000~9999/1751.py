import heapq

n = int(input())
q = [ int(input()) for _ in range(n) ]
heapq.heapify(q)
ans = 0

if len(q) == 1: 
    print(ans)
    
else:
    while len(q) > 1:
        temp = heapq.heappop(q) + heapq.heappop(q)
        heapq.heappush(q, temp)
        ans += temp
    print(ans)