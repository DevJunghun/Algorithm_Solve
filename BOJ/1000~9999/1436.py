n = int(input())
pattern = 666
count = 0

while True:
    if '666' in str(pattern): count += 1
    if count == n: 
        print(pattern)
        break
    pattern += 1