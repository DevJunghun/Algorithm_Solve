from collections import deque
import sys

n = int(sys.stdin.readline())
area = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, point, visited):
  q = deque()
  q.append((x, y))
  visited[x][y] = 1

  while q:
    a, b = q.popleft()

    for i in range(4):
      tx = a + dx[i]
      ty = b + dy[i]
      if (tx >= 0 and tx < n) and (ty >= 0 and ty < n):
        if area[tx][ty] > point and visited[tx][ty] == 0:
          visited[tx][ty] = 1
          q.append((tx, ty))

res = 0
max_point = max(map(max, area))
for i in range(max_point):
  cnt = 0
  visited = [ [0] * n for _ in range(n) ]
  
  for j in range(n):
    for k in range(n):
      if area[j][k] > i and visited[j][k] == 0:
        bfs(j, k, i, visited)
        cnt += 1
  
  if res < cnt:
    res = cnt

print(res)