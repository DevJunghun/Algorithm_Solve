import string

num = int(input())
result = num

for i in range(num):
    alphabet = string.ascii_lowercase
    alphabetList = list(alphabet)
    extraList = []
    a = input()

    alphabetList.remove(a[0])
    extraList.append(a[0])
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            if a[i] in alphabetList:
                alphabetList.remove(a[i])
                extraList.append(a[i])
            else:
                result -= 1
                break
        else:
            if a[i] in extraList:
                continue
            else:
                result -= 1
                break
print(result)