alist = list(map(int, input().split()))
answerlist = [1, 2, 3, 4, 5, 6, 7, 8]
reverselist = sorted(answerlist, reverse=True)

if alist == answerlist:
    print("ascending")
elif alist == reverselist:
    print("descending")
else:
    print("mixed")