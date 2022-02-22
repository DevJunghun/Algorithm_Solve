import sys
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(island, a, b):
  island[a][b] = 0
  q = deque()
  q.append([a, b])

  while q:
    x, y = q.popleft()
    for i in range(8):
      tx = x + dx[i]
      ty = y + dy[i]

      if (tx >= 0 and tx < h) and (ty >= 0 and ty < w) and island[tx][ty] == 1:
        island[tx][ty] = 0
        q.append([tx, ty])

while True:
  w, h = map(int, sys.stdin.readline().split())
  if w == 0 and h == 0: break

  island = [ list(map(int, sys.stdin.readline().split())) for _ in range(h) ]
  cnt = 0
  
  for i in range(h):
    for j in range(w):
      if island[i][j] == 1:
        bfs(island, i, j)
        cnt += 1
  
  print(cnt)