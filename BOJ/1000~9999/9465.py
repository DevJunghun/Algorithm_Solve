import sys

t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  sticker = [ list(map(int, sys.stdin.readline().split())) for _ in range(2) ]
  for j in range(1, n):
    if j == 1:
      sticker[0][j] += sticker[1][j - 1]
      sticker[1][j] += sticker[0][j - 1]
    else:
      sticker[0][j] += max(sticker[1][j - 1], sticker[1][j - 2])
      sticker[1][j] += max(sticker[0][j - 1], sticker[0][j - 2])

  print(max(sticker[0][-1], sticker[1][-1]))