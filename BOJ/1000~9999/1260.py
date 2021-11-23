import sys
import collections

def bfs(v, visited, graph):
    q = collections.deque()
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                visited[i] = 1
                q.append(i)

def dfs(v, visited, graph):
    visited[v] = 1
    print(v, end = " ")
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i, visited, graph)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
visited_1 = [0] * (n + 1)
visited_2 = [0] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs(v, visited_2, graph)
print()
bfs(v, visited_1, graph)
