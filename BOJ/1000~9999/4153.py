import sys

num_list = list()
while True:
    num_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    if num_list == [0, 0, 0]: break
    if num_list[0] ** 2 == (num_list[1] ** 2) + (num_list[2] ** 2): print('right')
    else: print('wrong')
