import sys

num = int(sys.stdin.readline())
meeting_list = [ tuple(map(int, sys.stdin.readline().split())) for i in range(num) ]
meeting_list.sort(key = lambda x: (x[1], x[0]))

count, end_time = 0, 0
for i in meeting_list:
    if end_time <= i[0]:
        count += 1
        end_time = i[1]
print(count)