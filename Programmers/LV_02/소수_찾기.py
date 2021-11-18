from itertools import permutations
import math

def solution(numbers):
    num_list = [ num for num in numbers ]
    temp_list, number_list = list(), list()
    sosu = 0
    for i in range(1, len(num_list) + 1):
        temp_list.append(list(set(permutations(num_list, i))))
    for i in temp_list:
        for j in i:
            number_list.append(int(''.join(j)))
    number_list = list(set(number_list))
    print(number_list)

    for i in number_list:
        if i == 0 or i == 1: continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0: break
        else: sosu += 1
    return sosu