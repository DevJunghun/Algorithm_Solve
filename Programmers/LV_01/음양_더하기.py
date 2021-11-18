def solution(absolutes, signs):
    s = 0
    for i in range(len(signs)):
        if signs[i] == True: s += absolutes[i]
        else: s += 0 - absolutes[i]
    return s