import sys

num = int(sys.stdin.readline())
point_list = [ tuple(map(int, sys.stdin.readline().split())) for i in range(num) ]
point_list.sort(key=lambda x: (x[1], x[0]))
for i in point_list:
    print(f"{i[0]} {i[1]}")