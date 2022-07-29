import sys

n, k = map(int, sys.stdin.readline().split())
result = 0

while bin(n).count('1') > k:
  n += 1
  result += 1

print(result) 
