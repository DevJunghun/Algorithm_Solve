def solution(s):
    pnum, ynum = 0, 0
    pnum = s.lower().count('p')
    ynum = s.lower().count('y')
        
    return pnum == ynum