num = int(input())
sum = 0
while num >= 0:
    if num % 5 == 0:
        sum += num // 5
        print(sum)
        break
    num -= 3
    sum += 1
else: print(-1)