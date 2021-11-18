import sys

a, b = map(int, sys.stdin.readline().rstrip("\n").split())
alist = list(map(int, sys.stdin.readline().rstrip("\n").split()))
result = []
for i in range(a):
    if alist[i] < b:
        result.append(str(alist[i]))

print(' '.join(result))