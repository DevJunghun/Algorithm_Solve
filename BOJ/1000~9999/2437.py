# 오름차순으로 정렬 후, 앞 원소부터 목표 가격과 비교하여 목표 가격이 더 작으면 목표 가격은 만들 수 없다.
import sys

n = int(sys.stdin.readline())
w_list = sorted(list(map(int, sys.stdin.readline().split())))
weight = 1
for i in range(len(w_list)):
  if weight < w_list[i]: break
  weight += w_list[i]
print(weight)