import sys

number = int(input())
number_list = [ int(sys.stdin.readline()) for i in range(number) ]
number_list.sort()
print(round(sum(number_list) / number))
print(number_list[number // 2])
print()