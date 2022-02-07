import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
p_list = [ int(sys.stdin.readline()) for _ in range(p) ]
docking_list = [ i for i in range(g + 1) ]

def union(a, b):
  a = find(a)
  b = find(b)
  docking_list[b] = a

def find(cur):
  if docking_list[cur] == cur: return cur
  docking_list[cur] = find(docking_list[cur])
  return docking_list[cur]

result = 0
for p in p_list:
  gate = find(p)
  if gate == 0: break
  result += 1
  union(gate - 1, gate)

print(result)