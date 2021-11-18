def solution(answers):
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    an1, an2, an3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == su1[i % 5]: an1 += 1
    for i in range(len(answers)):
        if answers[i] == su2[i % 8]: an2 += 1
    for i in range(len(answers)):
        if answers[i] == su3[i % 10]: an3 += 1
    
    a = [an1, an2, an3]
    res = list()
    for i in range(len(a)):
        if a[i] == max(a): res.append(i + 1)
            
    return res