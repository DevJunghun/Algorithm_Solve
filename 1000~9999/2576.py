numList = [int(input()) for i in range(7)]
oddList = []
for i in numList:
    if i % 2 != 0: oddList.append(i)

if len(oddList) != 0:
    print(sum(oddList))
    print(min(oddList))
else:
    print(-1)
