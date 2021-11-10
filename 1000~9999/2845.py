a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
for i in b:
    answer.append(str(i - a[0] * a[1]))

print(' '.join(answer))