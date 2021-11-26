import sys

n = int(sys.stdin.readline())
matrix_list = [ list(map(int, sys.stdin.readline().split(' '))) for i in range(n) ]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if matrix_list[j][i] and matrix_list[i][k]:
                matrix_list[j][k] = 1

for i in range(n):
    for j in matrix_list[i]:
        print(j, end=' ')
    print()
