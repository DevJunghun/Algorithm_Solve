def solution(clothes):
    res = {}
    for i in clothes:
        if i[1] in res: res[i[1]] += 1
        else: res[i[1]] = 1
    
    count = 1
    for i in res.values():
        count *= i + 1
    return count - 1