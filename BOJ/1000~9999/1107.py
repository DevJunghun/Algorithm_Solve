import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
trouble = list(map(int, sys.stdin.readline().split()))
count = abs(100 - n)

for i in range(1000001):
  i = str(i)
  for j in range(len(i)):
    if int(i[j]) in trouble: break
    elif j == len(i) - 1:
      count = min(count, abs(int(i) - n) + len(i))

print(count)
