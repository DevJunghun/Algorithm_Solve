import sys

n, m, p = (sys.stdin.readline().strip() for x in range(3))
cursor, count, answer = 0, 0, 0

while cursor < (int(m) - 1):
    if p[cursor:cursor+3] == 'IOI':
        count += 1
        if count == int(n):
            answer += 1
            count -= 1
        cursor += 2

    else:
        count = 0
        cursor += 1

print(answer)