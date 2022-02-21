import sys
from collections import deque

n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())
pair_list = [ [0] * (n + 1) for _ in range(n + 1) ]
for i in range(pair):
  a, b = map(int, sys.stdin.readline().split())
  pair_list[a][b] = pair_list[b][a] = 1

visited = [0] * (n + 1)
q = deque([1])
visited[1] = 1
infested = 0

while q:
  cur = q.popleft()
  for i in range(1, n + 1):
    if pair_list[cur][i] == 1 and visited[i] == 0:
      visited[i] = 1
      q.append(i)
      infested += 1

print(infested)

