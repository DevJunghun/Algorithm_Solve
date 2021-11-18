answer = 0
def DFS(numbers, target, idx, res):
    global answer
    if idx == len(numbers):
        if target == res:
            answer += 1
            return
    else:
        DFS(numbers, target, idx + 1, res + numbers[idx])
        DFS(numbers, target, idx + 1, res - numbers[idx])

def solution(numbers, target):
    global answer
    DFS(numbers, target, 0, 0)
    return answer