a = input()
num = 10
length = len(a)
print(a[:10])
while True:
    if length >= 0:
        print(a[num:num + 10])
    else:
        print(a[num:])
        break
    num += 10
    length -= 10