def solution(numbers):
    alist = list(map(str, numbers))
    alist.sort(key = lambda x : x * 3, reverse = True)
    return str(int(''.join(alist)))