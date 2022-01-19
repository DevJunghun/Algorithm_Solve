import sys

def fibonacci(number):
  if len(zero) <= number:
    for i in range(len(zero), number + 1):
      zero.append(zero[i - 1] + zero[i - 2])
      one.append(one[i - 1] + one[i - 2])
  print(f"{zero[number]} {one[number]}")

t = int(sys.stdin.readline())
n_list = [ int(sys.stdin.readline()) for _ in range(t) ]

zero = [1, 0, 1]
one = [0, 1, 1]

for i in n_list:
  fibonacci(i)