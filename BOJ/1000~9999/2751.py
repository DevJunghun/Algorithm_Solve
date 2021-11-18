import sys

number = int(input())
number_list = [ int(sys.stdin.readline()) for i in range(number) ]
sorted_number_list = sorted(number_list)
for i in sorted_number_list:
    print(i)