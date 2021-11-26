import sys

def check_house(a, b):
    global count
    if a < 0 or b < 0 or b >= num or a >= num or graph[a][b] == 0:
        return
    graph[a][b] = 0
    visited[a][b] = 1
    count += 1

    check_house(a + 1, b)
    check_house(a, b + 1)
    check_house(a - 1, b)
    check_house(a, b - 1)

if __name__ == '__main__':
    num = int(sys.stdin.readline())
    graph = [ list(map(int, sys.stdin.readline().strip())) for i in range(num) ]
    visited = [ [0] * num for _ in range(num) ]
    house_list = list()
    count = 0

    for i in range(num):
        for j in range(num):
            if visited[i][j] == 0 and graph[i][j] == 1:
                check_house(i, j)
                house_list.append(count)
                count = 0

    print(len(house_list))
    for i in sorted(house_list):
        print(i)