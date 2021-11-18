import sys

def factorial(n):
    if n == 0 or n == 1: return 1
    else: return n * factorial(n - 1)

a, b = map(int, sys.stdin.readline().split())
print(factorial(a) // (factorial(b) * factorial(a - b)))