day = int(input())
car_num = list(map(int, input().split()))
sum = 0
for i in car_num:
    if i == day: sum += 1
print(sum)