import itertools
from collections import deque

def solution(numbers, target):
    num_list = [ (i, -i) for i in numbers ]
    answer_list = list()
    answer_list.append(list(itertools.combinations(num_list, 1)))
    print(answer_list)