from collections import Counter

def solution(numbers):
    alist = list(range(10))
    a = Counter(numbers)
    s = 0
    for i in alist:
        if i not in a: s += i
    return s