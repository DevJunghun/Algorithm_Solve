a = input()
alphabetList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for i in a:
    for j in alphabetList:
        if i in j:
            result += alphabetList.index(j) + 3

print(result)