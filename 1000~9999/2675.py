a = int(input())
for i in range(a):
    alist = list(map(str, input().split()))
    alist[0] = int(alist[0])
    result = []
    for j in range(len(alist[1])):
        result.append(alist[0] * alist[1][j])
    print(''.join(result))