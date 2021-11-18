def solution(n):
    alist = ['1', '2', '4']
    res = ""
    while n > 0:
        n -= 1
        res = alist[n % 3] + res
        n = n // 3
    return res