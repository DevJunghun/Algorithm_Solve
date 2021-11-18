a = int(input())
count = 0
temp = a
while True:
    if temp < 10:
        b = temp
        num = (temp * 10) + (b % 10)
    else:
        b = (temp // 10) + (temp % 10)
        num = ((temp % 10) * 10) + (b % 10)

    temp = num
    count += 1
    if num == a:
        break

print(count)