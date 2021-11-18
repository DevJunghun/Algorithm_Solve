import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    trial = 0
    while scoville[0] < K:
        if len(scoville) <= 1: 
            trial = -1
            break
        heapq.heappush(scoville, (heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)))
        trial += 1
    return trial