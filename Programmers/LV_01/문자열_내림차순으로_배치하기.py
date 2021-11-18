def solution(s):
    alist = []
    answer = ''
    for i in s:
        alist.append(ord(i))
    alist.sort(reverse=True)
    for i in alist:
        answer += chr(i)
    return answer