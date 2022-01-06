import sys

equation = sys.stdin.readline()
equation = equation.replace('\n', '').split('-')

result = 0
for i in range(len(equation)):
    if i == 0:
        if '+' in equation[i]:
            temp = map(int, equation[i].split('+'))
            result += sum(temp)
        else:
            result += int(equation[i])
    else:
        if '+' in equation[i]:
            temp = map(int, equation[i].split('+'))
            result -= sum(temp)
        else:
            result -= int(equation[i])
print(result)