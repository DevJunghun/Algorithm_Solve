a = int(input())
line = 1
sumsum = 0
while True:
    if sumsum >= a:
        break
    sumsum = sum(range(line + 1))
    line += 1

line -= 1
rank = a - sum(range(line))
if line % 2 != 0:
    mother = rank
    son = (line + 1) - mother
    print("{}/{}".format(son, mother))
else:
    son = rank
    mother = (line + 1) - son
    print("{}/{}".format(son, mother))