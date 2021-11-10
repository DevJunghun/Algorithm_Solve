month, day = map(int, input().split())

num = 0
monthList = [31, 28 ,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(month - 1):
    num += monthList[i]
num = (num + day) % 7
print(yoil[num])