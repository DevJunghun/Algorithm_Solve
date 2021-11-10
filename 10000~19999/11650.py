import sys

num = int(input())
point_list = [tuple(map(int, sys.stdin.readline().split())) for i in range(num)]
point_list.sort(key = lambda x : (x[0], x[1]))
for i in range(num):
    print(f"{point_list[i][0]} {point_list[i][1]}")