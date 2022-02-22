import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(n + 1) ]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(node):
  visited[node] = 1
  for i in graph[node]:
    if visited[i] == 0: dfs(i)

for i in range(1, n + 1):
  if visited[i] == 0:
    dfs(i)
    cnt += 1

print(cnt)