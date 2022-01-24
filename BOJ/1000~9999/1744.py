import sys

n = int(sys.stdin.readline())
num_list = [ int(sys.stdin.readline()) for _ in range(n) ]
p_list = sorted([ num_list[i] for i in range(n) if num_list[i] > 1 ])
n_list = sorted([ num_list[i] for i in range(n) if num_list[i] < 0 ], reverse=True)
zero_list = [ num_list[i] for i in range(n) if num_list[i] == 0 ]
one_list = [ num_list[i] for i in range(n) if num_list[i] == 1 ]
res = 0

while p_list:
  if len(p_list) != 1: res += p_list.pop() * p_list.pop()
  else: res += p_list.pop()

while n_list:
  if len(n_list) != 1: res += n_list.pop() * n_list.pop()
  else: 
    if zero_list:
      res += n_list.pop() * zero_list.pop()
    else:
      res += n_list.pop()

while one_list:
  res += one_list.pop()

print(res)