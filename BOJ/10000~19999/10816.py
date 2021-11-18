from collections import Counter
import sys

num1 = int(input())
card_list = sys.stdin.readline().split()
num2 = int(input())
count_list = sys.stdin.readline().split()

C = Counter(card_list)
print(' '.join(f'{C[m]}' if m in C else '0' for m in count_list))