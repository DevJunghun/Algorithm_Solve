def solution(n):
    charList = ["수", "박"]
    answerList = []
    num = 0
    answer = ""
    
    for i in range(0, n):
        if n % 2 == 0:
            num = i % 2
            answerList.append(charList[num])
        else:
            num = i % 2
            answerList.append(charList[num])
            
    for i in answerList:
        answer += i
        
    return answer