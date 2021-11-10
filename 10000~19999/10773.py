from collections import deque

num = int(input())
stack = deque([])
for i in range(num):
    a = int(input())
    if a != 0: stack.append(a)
    else: stack.pop()
print(sum(stack))