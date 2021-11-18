def solution(arr):
    mini = min(arr)
    arr.remove(mini)
    if len(arr) == 0:
        arr.append(-1)
    
    return arr