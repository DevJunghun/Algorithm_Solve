a = int(input())
alist = list(map(int, input().split()))
max = max(alist)

for i in range(a):
    alist[i] = alist[i] / max * 100

print(sum(alist) / a)