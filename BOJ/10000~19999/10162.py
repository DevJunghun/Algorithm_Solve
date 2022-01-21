t = int(input())
time_list = [300, 60, 10]
answer_list = [0, 0, 0]
for i in range(len(time_list)):
  if t % 10 != 0: break
  answer_list[i] = t // time_list[i]
  t -= time_list[i] * answer_list[i]

if answer_list.count(0) == 3: print(-1)
else: print(' '.join(map(str, answer_list)))