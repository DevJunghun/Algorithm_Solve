import sys

n = int(sys.stdin.readline())
temp = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ]
test_case = [ pow(a, b, 10) for a, b in temp ]

for i in test_case:
  if i == 0: print(10)
  else: print(i)