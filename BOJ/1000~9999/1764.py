import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
d_list = [ sys.stdin.readline().strip() for _ in range(n) ]
b_list = [ sys.stdin.readline().strip() for _ in range(m) ]
db_list = list()

db_dic = Counter(d_list + b_list)
for i in db_dic:
    if db_dic[i] >= 2: db_list.append(i)

db_list.sort()
print(len(db_list))
for name in db_list: print(name)
