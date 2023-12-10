import sys

input = int(input())
for i in range(input):
    sentence = sys.stdin.readline().rstrip()
    stack = []
    for j in sentence:
        if j == "(":
            stack.append(j)
        else:
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                stack.pop()
    print("YES") if len(stack) == 0 else print("NO")