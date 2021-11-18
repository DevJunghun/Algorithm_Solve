def solution(x):
    x = str(x)
    snum = 0 
    for i in x:
        snum += int(i)
    x = int(x)
    if x % snum == 0:
        return True
    else:
        return False