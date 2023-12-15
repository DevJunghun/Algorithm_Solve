def solution(cards1, cards2, goal):
    a=0
    for i in goal:
        if i in cards1[0]:
            a+=1
            del cards1[0]
            if len(cards1)==0:
                cards1.append("0")
        elif i in cards2[0]:
            a+=1
            del cards2[0]
            if len(cards2)==0:
                cards2.append("0")
    if a==len(goal):
        return 'Yes'
    return 'No'