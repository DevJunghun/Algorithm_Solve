sum = 0
for i in range(8):
    a = input()
    for j in range(len(a)):
        if i % 2 == 0 and j % 2 == 0 and a[j] == 'F':
            sum += 1
        elif i % 2 != 0 and j % 2 != 0 and a[j] == 'F':
            sum += 1
print(sum)