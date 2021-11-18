def solution(arr):
    sums = 0
    for i in range(len(arr)):
        sums += arr[i]
    
    aver = sums / len(arr)
    return aver