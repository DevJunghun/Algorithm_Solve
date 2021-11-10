a = input()
alphalist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for word in alphalist:
    a = a.replace(word, '*')
print(len(a))