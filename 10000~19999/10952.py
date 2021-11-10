import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip("\n").split())
    if a != 0 and b != 0:
        print(a + b)
    else:
        break
