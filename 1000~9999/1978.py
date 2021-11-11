import sys
import math

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
count = 0
for i in num_list:
    if i <= 1: continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0: break
    else: count += 1
print(count)