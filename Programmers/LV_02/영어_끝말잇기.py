def solution(n, words):
    fail_person, fail_try = 0, 0
    for word in range(1, len(words)):
        if len(words[0]) <= 1:
            fail_person = 1
            break
        elif (words[word][0] != words[word - 1][-1]) or (words[word] in words[:word]) or (len(words) <= 1):
            fail_person = (word % n) + 1
            fail_try = word // n + 1
            break
    if len(words[-1]) <= 1:
        fail_person, fail_try = n if len(words) % n == 0 else len(words) % n, 0
        
    return [fail_person, fail_try]