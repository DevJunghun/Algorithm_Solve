import sys

num = int(sys.stdin.readline())
alist = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
blist = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(num):
    result += alist[i] * blist.pop(blist.index(min(blist)))
print(result)