from itertools import combinations
import math

def solution(nums):
    a = list(map(sum, combinations(nums, 3)))
    sosu = 0
    for i in a:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0: break
        else: sosu += 1
    return sosu