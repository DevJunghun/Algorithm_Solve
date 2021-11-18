def solution(prices):
    time_list = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]: 
                time_list[i] += 1
            else: 
                break
    return time_list