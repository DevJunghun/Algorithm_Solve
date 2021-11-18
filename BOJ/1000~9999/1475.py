import math

a = input().replace('6', '9')
aset = set([a[i] for i in range(len(a))])
max = 0
max6 = 0
for i in aset:
    if i == '9':
        if max6 <= math.ceil(a.count(i) / 2): max6 = math.ceil(a.count(i) / 2)
    else:
        if max <= a.count(i): max = a.count(i)
print(max if max > max6 else max6)