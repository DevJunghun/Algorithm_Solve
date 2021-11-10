a, b = map(int, input().split())

if a == 0:
    if b < 45:
        a = 23
        b += 15
    else:
        b -= 45

else:
    if b < 45:
        a -= 1
        b += 15
    else:
        b -= 45
print(a, b)