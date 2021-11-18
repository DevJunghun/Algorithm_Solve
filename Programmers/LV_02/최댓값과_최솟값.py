def solution(s):
    answer = list(map(int, s.split()))
    return "%d %d" %(min(answer), max(answer))