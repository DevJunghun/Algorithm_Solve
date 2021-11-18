import collections

def solution(participant, completion):
    alist = collections.Counter(participant) - collections.Counter(completion)
    return list(alist)[0]