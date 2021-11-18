def solution(n):
    number = str(n)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum