alist = list(map(int, input().split()))
if alist[2] - alist[1] > 0:
    print(alist[0] // (alist[2] - alist[1]) + 1)
else:
    print(-1)