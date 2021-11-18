import sys

count_list = [0] * 10001
num = int(sys.stdin.readline())
for i in range(num):
    count_list[int(sys.stdin.readline())] += 1
for i in range(len(count_list)):
    if count_list[i] != 0: 
        for j in range(count_list[i]):
             sys.stdout.write(str(i) + '\n')