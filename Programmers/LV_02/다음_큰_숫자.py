def solution(n):
    answer = 0
    a = 0
    b = 0
    for i in range(n+1, 1000001):
        a = str(bin(n))
        b = str(bin(i))
        if a.count('1') == b.count('1'):
            answer = i
            break
    return answer