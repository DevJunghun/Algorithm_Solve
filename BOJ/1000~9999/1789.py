n = int(input())
res = 1
while ((res * (res + 1)) / 2) <= n:
  res += 1

print(res - 1)