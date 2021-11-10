a = int(input())
for i in range(a):
    new_list = []
    student = list(map(int, input().split()))
    avg = sum(student[1:]) / student[0]
    for j in range(1, student[0] + 1):
        if student[j] > avg: new_list.append(student[j])
    rate = round(len(new_list) * 100 / student[0], 3)
    print("{:.3f}%".format(rate))