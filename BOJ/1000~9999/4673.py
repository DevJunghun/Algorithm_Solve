numbers = set(range(1, 10001))
con = set()
for num in numbers:
  for n in str(num):
    num += int(n)
  con.add(num)

self_number = numbers - con
for self_num in sorted(self_number):
  print(self_num)