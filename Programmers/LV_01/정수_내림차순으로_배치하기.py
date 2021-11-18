def solution(n):
    n = sorted(str(n))
    n = int("".join(reversed(n)))
    
    return n