import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip("\n").split())
    except:
        break
    print(a + b)