import sys
import heapq

def prim(graph, node, visited):
    count, answer = 0, 0
    heap = [[0, 1]]

    while heap:
        if count == node: break
        weight, v = heapq.heappop(heap)
        if visited[v] == 0:
            visited[v] = 1
            count += 1
            answer += weight
            
            for i in graph[v]:
                heapq.heappush(heap, i)
    return answer

node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]
visited = [0] * (node + 1)

for i in range(edge):
    v, u, w = map(int, sys.stdin.readline().split())
    graph[v].append([w, u])
    graph[u].append([w, v])
    
print(prim(graph, node, visited))