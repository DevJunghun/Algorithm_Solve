import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n) ]
visited = [ [0] * m for _ in range(n) ]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

q = deque([(0, 0)])
visited[0][0] = 1

while q:
  x, y = q.popleft()
  if x == n-1 and y == m-1:
    print(visited[x][y])
    break
  
  for i in range(4):
    tx = x + dx[i]
    ty = y + dy[i]

    if (tx >= 0 and tx < n) and (ty >= 0 and ty < m):
      if visited[tx][ty] == 0 and maze[tx][ty] == 1:
        visited[tx][ty] = visited[x][y] + 1
        q.append((tx, ty))