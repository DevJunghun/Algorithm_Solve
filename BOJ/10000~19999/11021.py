import sys

a = int(sys.stdin.readline().rstrip("\n"))
for i in range(a):
    b, c = map(int, sys.stdin.readline().rstrip("\n").split())
    print("Case #{}: {}".format(i + 1, b + c))
