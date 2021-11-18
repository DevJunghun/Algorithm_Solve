a = input().upper()
alist = list(set(a))
blist = []
result = []

for i in alist:
    blist.append(a.count(i))
for i in blist:
    if i == max(blist):
        result.append(blist.index(i))

if len(result) == 1: print(alist[blist.index(max(blist))])
else: print("?")