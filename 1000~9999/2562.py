max = 0
index = 0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        index = i
    else:
        continue

print("{}\n{}".format(max, index + 1))