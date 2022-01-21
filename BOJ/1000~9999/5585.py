n = 1000 - int(input())
money_list = [500, 100, 50, 10, 5, 1]
count_list = [0] * len(money_list)

for i in range(len(money_list)):
  if n <= 0: break
  count_list[i] = n // money_list[i]
  n %= money_list[i]
print(sum(count_list))