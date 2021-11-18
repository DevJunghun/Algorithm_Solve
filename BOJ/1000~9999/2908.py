a = list(map(str, input().split()))
num1 = int(''.join(reversed(a[0])))
num2 = int(''.join(reversed(a[1])))
print(num1) if num1 > num2 else print(num2)