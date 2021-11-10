import sys

num = int(input())
alist = [tuple(sys.stdin.readline().split()) for i in range(num)]
alist.sort(key = lambda x : (int(x[0])))

for i in alist:
    print(f"{i[0]} {i[1]}")