n = int(input())
people = sorted([ int(input()) for _ in range(n) ], reverse = True)
tip = 0

for i in range(n):
    if people[i] - i >= 0:
        tip += people[i] - i

print(tip)