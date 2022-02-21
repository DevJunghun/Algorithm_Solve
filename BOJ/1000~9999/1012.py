import sys
from collections import deque

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(visited, x, y):
  q = deque([(x, y)])
  visited[x][y] = 0

  while q:
    nx, ny = q.popleft()
            
    for i in range(4):
      tx = nx + dx[i]
      ty = ny + dy[i]

      if (tx >= 0 and tx < n) and (ty >= 0 and ty < m) and visited[tx][ty] == 1:
        visited[tx][ty] = 0
        q.append((tx, ty))
  
t = int(sys.stdin.readline())
for _ in range(t):
  n, m, k = map(int, sys.stdin.readline().split())
  visited = [ [0] * m for _ in range(n) ]
  cnt = 0
  
  for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    visited[x][y] = 1

  for a in range(n):
    for b in range(m):
      if visited[a][b] == 1:
        bfs(visited, a, b)
        cnt += 1

  print(cnt)