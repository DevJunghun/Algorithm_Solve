a = int(input())
numberofO = 0
for i in range(a):
    sum = 0
    numberofO = 0
    result = input()
    for j in range(len(result)):
        if result[j] == 'O':
            numberofO += 1
            sum += numberofO
        else:
            numberofO = 0
    print(sum)