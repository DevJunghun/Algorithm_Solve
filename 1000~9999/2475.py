a = list(map(int, input().split()))
print(sum(list(map(lambda x: x ** 2, a))) % 10)