import sys

n = int(input())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == i:
            print(1)
            break
        elif n_list[mid] < i:
            left = mid + 1
        elif n_list[mid] > i:
            right = mid - 1
    else: print(0)