import sys

n, k = map(int, sys.stdin.readline().split())
student_list = list(map(int, sys.stdin.readline().split()))
height_compare = sorted([ student_list[i] - student_list[i - 1] for i in range(1, n) ])
print(sum(height_compare[:n - k]))