import sys

n, m = map(int, sys.stdin.readline().split())
distance = list(map(int, sys.stdin.readline().split()))
plus_distance, minus_distance = [], []
for i in distance:
  if i > 0: plus_distance.append(i)
  else: minus_distance.append(i)

result = 0
max_distance = max(map(abs, distance))
plus_distance.sort(reverse=True)
minus_distance.sort()

answer_list = []

for i in range(0, len(plus_distance), m):
  if plus_distance[i] != max_distance:
    answer_list.append(plus_distance[i])

for i in range(0, len(minus_distance), m):
  if abs(minus_distance[i]) != max_distance:
    answer_list.append(abs(minus_distance[i]))

result += max_distance
for i in answer_list:
  result += i * 2

print(result)