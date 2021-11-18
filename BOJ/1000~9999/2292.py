a = int(input())
count = 1

if a == 1:
    print(1)
for i in range(1, a):
    count = count + 6 * i
    if a <= count:
        print(i + 1)
        break