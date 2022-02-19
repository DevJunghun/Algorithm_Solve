import sys

n = int(sys.stdin.readline())
rope = sorted([ int(sys.stdin.readline()) for _ in range(n) ], reverse=True)
weight = []
for i in range(len(rope)):
  weight.append(rope[i] * (i + 1))

print(max(weight))