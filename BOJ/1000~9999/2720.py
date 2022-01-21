import sys

t = int(sys.stdin.readline())
price_list = [ int(sys.stdin.readline()) for _ in range(t) ]
money_list = [25, 10, 5, 1]
count_list = [0] * len(money_list)

for price in price_list:
  for i in range(len(money_list)):
    count_list[i] = price // money_list[i]
    price %= money_list[i]

  print(' '.join(map(str, count_list)))