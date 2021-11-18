def solution(numbers):
    res = list()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            res.append(numbers[i] + numbers[j])
    return sorted(list(set(res)))