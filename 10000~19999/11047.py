import sys

num, price = map(int, sys.stdin.readline().split())
money_list = list(reversed(sorted([ int(sys.stdin.readline()) for money in range(num) ])))
idx, count = 0, 0
while price > 0:
    if price // money_list[idx] >= 1:
        count += price // money_list[idx]
        price = price % money_list[idx]
    idx += 1
print(count)