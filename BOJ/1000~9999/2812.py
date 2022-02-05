import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))
stack = []
target_num = k

for i in range(n):
  while target_num > 0 and stack:
    if stack[len(stack) - 1] < num[i]:
      stack.pop()
      target_num -= 1
    else:
      break
  
  stack.append(num[i])

print(''.join(map(str, stack[:n - k])))