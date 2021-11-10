modSet = []
for i in range(10):
    modSet.append(int(input()) % 42)

modSet = set(modSet)
print(len(modSet))
