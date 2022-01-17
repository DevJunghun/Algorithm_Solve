import sys

num = int(sys.stdin.readline())
people_list = list(map(int, sys.stdin.readline().split()))
people = list()
for n, p in enumerate(people_list):
  people.append((n + 1, p))
people.sort(key = lambda x:x[1])

prev_time = people[0][1]
sum_time = prev_time
for i in range(1, len(people)):
  now_time = prev_time + people[i][1]
  prev_time = now_time
  sum_time += now_time
print(sum_time)