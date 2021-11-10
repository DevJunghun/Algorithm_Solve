a = input()
b = input()

num1 = int(a) * int(b[2])
num2 = int(a) * int(b[1])
num3 = int(a) * int(b[0])
result = num1 + (num2 * 10) + (num3 * 100)

print("{}\n{}\n{}\n{}".format(num1, num2, num3, result))