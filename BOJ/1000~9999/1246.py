import sys

n, m = map(int, sys.stdin.readline().split())
p_list = sorted([ int(sys.stdin.readline().replace('\n', '')) for _ in range(m) ])

max_price = (0, 0)
for i in range(len(p_list)):
    if len(p_list[i:]) > n:
        continue
    else:
        max_price = max(max_price, (len(p_list[i:]) * p_list[i], p_list[i]))
print(f"{max_price[1]} {max_price[0]}")