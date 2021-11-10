a = list(map(int, input().split()))
b = [1, 1, 2, 2, 2, 8]
answer = []

for i, j in zip(a, b):
    answer.append(str(j - i))
print(' '.join(answer))
0