import sys

n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
result = [0] * n

for i in range(n):
  cnt = 0
  for j in range(n):
    if result[j] == 0 and cnt == people[i]:
      result[j] = i + 1
      break
    elif result[j] == 0:
      cnt += 1

print(*result)