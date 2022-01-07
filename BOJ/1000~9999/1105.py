import sys

l, r = sys.stdin.readline().split()
cnt = 0
if len(l) != len(r): print(cnt)
else:
    for i in range(len(l)):
        if l[i] != r[i]: break
        else:
            if l[i] == '8': cnt += 1
    print(cnt)
